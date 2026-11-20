"""Minimal SVG and PNG writers (stdlib only: math, zlib, struct)."""

from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path


def _lin(x, x0, x1, p0, p1) -> float:
    return p0 + (p1 - p0) * (x - x0) / (x1 - x0)


def _log_map(x, x0, x1, p0, p1) -> float:
    return _lin(math.log10(x), math.log10(x0), math.log10(x1), p0, p1)


# Distinct, colour-blind-friendlier stroke colours (sRGB).
TISSUE_COLORS = {
    "Muscle": (0x1F, 0x4E, 0x79),
    "Skin (dry)": (0xC4, 0x59, 0x11),
    "Skin (wet)": (0x54, 0x8C, 0x2F),
    "Fat (not infiltrated)": (0x70, 0x30, 0xA0),
    "Fat (infiltrated)": (0x7F, 0x60, 0x00),
}


def write_svg(
    path: Path,
    series: dict[str, list[tuple[float, float]]],
    *,
    freq_min: float,
    freq_max: float,
    depth_min: float,
    depth_max: float,
    band_markers: list[tuple[float, str]],
    title: str,
    subtitle: str,
) -> None:
    w, h = 960, 620
    l, r, t, b = 80, 40, 60, 70
    def xmap(f): return _log_map(f, freq_min, freq_max, l, w - r)
    def ymap(d): return _log_map(d, depth_min, depth_max, h - b, t)

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{w/2:.1f}" y="24" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="bold">{_esc(title)}</text>',
        f'<text x="{w/2:.1f}" y="44" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#333">{_esc(subtitle)}</text>',
        f'<rect x="{l}" y="{t}" width="{w-r-l}" height="{h-b-t}" fill="#fafafa" stroke="#222"/>',
    ]
    # Log grid
    exp_f0, exp_f1 = int(math.floor(math.log10(freq_min))), int(math.ceil(math.log10(freq_max)))
    exp_d0, exp_d1 = int(math.floor(math.log10(depth_min))), int(math.ceil(math.log10(depth_max)))
    for e in range(exp_f0, exp_f1 + 1):
        for m in range(1, 10):
            f = 10 ** e * m
            if not (freq_min <= f <= freq_max):
                continue
            x = xmap(f)
            stroke = "#cccccc" if m != 1 else "#999999"
            parts.append(f'<line x1="{x:.2f}" y1="{t}" x2="{x:.2f}" y2="{h-b}" stroke="{stroke}" stroke-width="0.6"/>')
            if m == 1:
                parts.append(
                    f'<text x="{x:.2f}" y="{h-b+18}" text-anchor="middle" font-family="sans-serif" font-size="10">{_freq_label(f)}</text>'
                )
    for e in range(exp_d0, exp_d1 + 1):
        for m in range(1, 10):
            d = 10 ** e * m
            if not (depth_min <= d <= depth_max):
                continue
            y = ymap(d)
            stroke = "#cccccc" if m != 1 else "#999999"
            parts.append(f'<line x1="{l}" y1="{y:.2f}" x2="{w-r}" y2="{y:.2f}" stroke="{stroke}" stroke-width="0.6"/>')
            if m == 1:
                parts.append(
                    f'<text x="{l-8}" y="{y+4:.2f}" text-anchor="end" font-family="sans-serif" font-size="10">{_len_label(d)}</text>'
                )
    # Band markers (behind curves)
    for f, _label in band_markers:
        if freq_min <= f <= freq_max:
            x = xmap(f)
            parts.append(
                f'<line x1="{x:.2f}" y1="{t}" x2="{x:.2f}" y2="{h-b}" '
                f'stroke="#888888" stroke-width="0.8" stroke-dasharray="3 3"/>'
            )
    # Curves
    legend_y = t + 14
    for name, pts in series.items():
        rgb = TISSUE_COLORS.get(name, (0, 0, 0))
        color = f"rgb({rgb[0]},{rgb[1]},{rgb[2]})"
        coords = []
        for f, d in pts:
            if d <= 0 or not math.isfinite(d):
                continue
            if f < freq_min or f > freq_max:
                continue
            dclip = min(max(d, depth_min), depth_max)
            coords.append(f"{xmap(f):.2f},{ymap(dclip):.2f}")
        if coords:
            parts.append(
                f'<polyline fill="none" stroke="{color}" stroke-width="2" points="{" ".join(coords)}"/>'
            )
        parts.append(
            f'<rect x="{l+8}" y="{legend_y-8}" width="12" height="8" fill="{color}"/>'
            f'<text x="{l+24}" y="{legend_y}" font-family="sans-serif" font-size="11">{_esc(name)}</text>'
        )
        legend_y += 16
    parts.append(
        f'<text x="{(l+w-r)/2:.1f}" y="{h-16}" text-anchor="middle" font-family="sans-serif" font-size="12">Frequency</text>'
    )
    parts.append(
        f'<text x="18" y="{(t+h-b)/2:.1f}" text-anchor="middle" font-family="sans-serif" font-size="12" '
        f'transform="rotate(-90 18 {(t+h-b)/2:.1f})">Field skin depth</text>'
    )
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _freq_label(f: float) -> str:
    if f >= 1e9:
        v = f / 1e9
        return f"{v:.0f} GHz" if abs(v - round(v)) < 1e-9 else f"{v:g} GHz"
    if f >= 1e6:
        v = f / 1e6
        return f"{v:.0f} MHz" if abs(v - round(v)) < 1e-9 else f"{v:g} MHz"
    return f"{f:g} Hz"


def _len_label(d: float) -> str:
    if d >= 1:
        return f"{d:g} m"
    if d >= 1e-2:
        return f"{d*100:g} cm"
    if d >= 1e-3:
        return f"{d*1e3:g} mm"
    return f"{d*1e3:g} mm"


def write_png_from_svg_raster(
    path: Path,
    series: dict[str, list[tuple[float, float]]],
    *,
    freq_min: float,
    freq_max: float,
    depth_min: float,
    depth_max: float,
    band_markers: list[tuple[float, str]],
    title: str,
    subtitle: str,
) -> None:
    """A simple raster of the same log-log chart (no matplotlib)."""
    w, h = 960, 620
    l, r, t, b = 80, 40, 60, 70
    pixels = bytearray([255, 255, 255] * w * h)

    def setp(x, y, rgb, a=255):
        if a <= 0:
            return
        xi, yi = int(round(x)), int(round(y))
        if not (0 <= xi < w and 0 <= yi < h):
            return
        i = (yi * w + xi) * 3
        if a >= 255:
            pixels[i:i+3] = bytes(rgb)
            return
        inv = 255 - a
        pixels[i] = (pixels[i] * inv + rgb[0] * a) // 255
        pixels[i+1] = (pixels[i+1] * inv + rgb[1] * a) // 255
        pixels[i+2] = (pixels[i+2] * inv + rgb[2] * a) // 255

    def line(x0, y0, x1, y1, rgb, width=1):
        dx, dy = x1 - x0, y1 - y0
        n = max(int(math.hypot(dx, dy)) * 2, 1)
        for i in range(n + 1):
            x = x0 + dx * i / n
            y = y0 + dy * i / n
            setp(x, y, rgb)
            if width >= 2:
                setp(x + 1, y, rgb)
                setp(x, y + 1, rgb)

    def xmap(f): return _log_map(f, freq_min, freq_max, l, w - r)
    def ymap(d): return _log_map(d, depth_min, depth_max, h - b, t)

    # Plot background
    for y in range(t, h - b):
        for x in range(l, w - r):
            setp(x, y, (250, 250, 250))
    # Grid
    exp_f0, exp_f1 = int(math.floor(math.log10(freq_min))), int(math.ceil(math.log10(freq_max)))
    exp_d0, exp_d1 = int(math.floor(math.log10(depth_min))), int(math.ceil(math.log10(depth_max)))
    for e in range(exp_f0, exp_f1 + 1):
        for m in range(1, 10):
            f = 10 ** e * m
            if freq_min <= f <= freq_max:
                col = (150, 150, 150) if m == 1 else (204, 204, 204)
                x = xmap(f)
                line(x, t, x, h - b, col)
    for e in range(exp_d0, exp_d1 + 1):
        for m in range(1, 10):
            d = 10 ** e * m
            if depth_min <= d <= depth_max:
                col = (150, 150, 150) if m == 1 else (204, 204, 204)
                y = ymap(d)
                line(l, y, w - r, y, col)
    line(l, t, w - r, t, (34, 34, 34))
    line(l, h - b, w - r, h - b, (34, 34, 34))
    line(l, t, l, h - b, (34, 34, 34))
    line(w - r, t, w - r, h - b, (34, 34, 34))
    for e in range(exp_f0, exp_f1 + 1):
        f = 10 ** e
        if freq_min <= f <= freq_max:
            _draw_text(pixels, w, h, _freq_label(f), x=xmap(f), y=h - b + 6, rgb=(0, 0, 0), scale=1, center=True)
    for e in range(exp_d0, exp_d1 + 1):
        d = 10 ** e
        if depth_min <= d <= depth_max:
            _draw_text(pixels, w, h, _len_label(d), x=8, y=int(ymap(d) - 3), rgb=(0, 0, 0), scale=1, center=False)
    for f, _label in band_markers:
        if freq_min <= f <= freq_max:
            x = xmap(f)
            # dashed
            y = t
            while y < h - b:
                line(x, y, x, min(y + 3, h - b), (136, 136, 136))
                y += 6
    for name, pts in series.items():
        rgb = TISSUE_COLORS.get(name, (0, 0, 0))
        prev = None
        for f, d in pts:
            if d <= 0 or not math.isfinite(d) or not (freq_min <= f <= freq_max):
                prev = None
                continue
            dclip = min(max(d, depth_min), depth_max)
            pt = (xmap(f), ymap(dclip))
            if prev is not None:
                line(prev[0], prev[1], pt[0], pt[1], rgb, width=2)
            prev = pt
    # Very small built-in 5x7 font for title (ASCII)
    _draw_text(pixels, w, h, title, x=w // 2, y=16, rgb=(0, 0, 0), scale=2, center=True)
    _draw_text(pixels, w, h, "Field skin depth vs frequency (log-log). Dashed: product bands.",
               x=w // 2, y=34, rgb=(40, 40, 40), scale=1, center=True)
    _draw_text(pixels, w, h, "Frequency", x=w // 2, y=h - 22, rgb=(0, 0, 0), scale=1, center=True)
    # Legend
    ly = t + 8
    for name in series:
        rgb = TISSUE_COLORS.get(name, (0, 0, 0))
        for dx in range(12):
            for dy in range(6):
                setp(l + 8 + dx, ly + dy, rgb)
        _draw_text(pixels, w, h, name, x=l + 24, y=ly - 1, rgb=(0, 0, 0), scale=1, center=False)
        ly += 12
    path.write_bytes(_pack_png(pixels, w, h))


# 5x7 uppercase-friendly bitmap font (ASCII 32-126), row-major, 5 bits per row.
_FONT = None


def _font():
    global _FONT
    if _FONT is not None:
        return _FONT
    # Compact encoding: 7 bytes per glyph, columns packed in low 5 bits of each row.
    raw = {}
    def g(ch, rows):
        raw[ord(ch)] = rows
    # Minimal set used in titles and labels
    glyphs = {
        " ": [0]*7,
        "-": [0,0,0,31,0,0,0],
        ".": [0,0,0,0,0,6,6],
        "/": [1,2,2,4,8,8,16],
        "0": [14,17,19,21,25,17,14],
        "1": [4,12,4,4,4,4,14],
        "2": [14,17,1,2,4,8,31],
        "3": [14,17,1,6,1,17,14],
        "4": [2,6,10,18,31,2,2],
        "5": [31,16,30,1,1,17,14],
        "6": [14,16,16,30,17,17,14],
        "7": [31,1,2,4,8,8,8],
        "8": [14,17,17,14,17,17,14],
        "9": [14,17,17,15,1,1,14],
        ":": [0,6,6,0,6,6,0],
        "(": [4,8,16,16,16,8,4],
        ")": [8,4,2,2,2,4,8],
        "A": [14,17,17,31,17,17,17],
        "B": [30,17,17,30,17,17,30],
        "C": [14,17,16,16,16,17,14],
        "D": [30,17,17,17,17,17,30],
        "E": [31,16,16,30,16,16,31],
        "F": [31,16,16,30,16,16,16],
        "G": [14,17,16,19,17,17,15],
        "H": [17,17,17,31,17,17,17],
        "I": [14,4,4,4,4,4,14],
        "J": [1,1,1,1,1,17,14],
        "K": [17,18,20,24,20,18,17],
        "L": [16,16,16,16,16,16,31],
        "M": [17,27,21,21,17,17,17],
        "N": [17,17,25,21,19,17,17],
        "O": [14,17,17,17,17,17,14],
        "P": [30,17,17,30,16,16,16],
        "Q": [14,17,17,17,21,18,13],
        "R": [30,17,17,30,20,18,17],
        "S": [14,17,16,14,1,17,14],
        "T": [31,4,4,4,4,4,4],
        "U": [17,17,17,17,17,17,14],
        "V": [17,17,17,17,17,10,4],
        "W": [17,17,17,21,21,21,10],
        "X": [17,17,10,4,10,17,17],
        "Y": [17,17,10,4,4,4,4],
        "Z": [31,1,2,4,8,16,31],
    }
    _FONT = {ord(k): v for k, v in glyphs.items()}
    return _FONT


def _draw_text(pixels, w, h, text, *, x, y, rgb, scale=1, center=False):
    font = _font()
    # only printable mapped glyphs; lowercase -> upper
    chars = []
    for ch in text:
        o = ord(ch.upper() if ch.isascii() and ch.isalpha() else ch)
        if o not in font:
            o = ord("-") if ch == "_" else ord(" ")
        chars.append(o)
    tw = len(chars) * (5 * scale + scale)
    start = int(x - tw / 2) if center else int(x)
    py = int(y)
    for i, o in enumerate(chars):
        rows = font[o]
        ox = start + i * (5 * scale + scale)
        for ry, bits in enumerate(rows):
            for cx in range(5):
                if bits & (1 << (4 - cx)):
                    for sy in range(scale):
                        for sx in range(scale):
                            xi = ox + cx * scale + sx
                            yi = py + ry * scale + sy
                            if 0 <= xi < w and 0 <= yi < h:
                                i3 = (yi * w + xi) * 3
                                pixels[i3:i3+3] = bytes(rgb)


def _pack_png(pixels: bytearray, w: int, h: int) -> bytes:
    def chunk(tag: bytes, data: bytes) -> bytes:
        crc = zlib.crc32(tag + data) & 0xFFFFFFFF
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc)

    raw = bytearray()
    row = w * 3
    for y in range(h):
        raw.append(0)
        raw.extend(pixels[y * row:(y + 1) * row])
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + chunk(b"IEND", b"")
    )
