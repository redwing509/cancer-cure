"""Representative product-band frequencies from opened allocation records.

Every edge below was copied from a page opened on 19 Nov 2026 (Pacific
Time). The representative frequency is the arithmetic midpoint of a single
opened interval, or is otherwise identified in `note`. These midpoints are
not claimed to be the only, or the most used, channel in the service.

Sources (all opened the same day):

* 47 CFR § 18.301, eCFR:
  https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-18/subpart-C/section-18.301
* 47 CFR § 22.905, eCFR:
  https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-22/subpart-H/section-22.905
* 47 CFR § 24.229, LII copy of the e-CFR:
  https://www.law.cornell.edu/cfr/text/47/24.229
* 47 CFR § 15.247, LII:
  https://www.law.cornell.edu/cfr/text/47/15.247
* 47 CFR § 15.407, LII:
  https://www.law.cornell.edu/cfr/text/47/15.407
* 47 CFR § 27.5, LII:
  https://www.law.cornell.edu/cfr/text/47/27.5
* 47 CFR § 30.4, LII:
  https://www.law.cornell.edu/cfr/text/47/30.4

eCFR pages for §§ 15.247, 15.407, 24.229 and 30.4 returned a CAPTCHA /
"Request Access" block later the same day; the LII copies of those four
sections were used instead and are cited as such.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Band:
    key: str
    service: str
    freq_hz: float
    opened_range: str
    source_url: str
    citation: str
    note: str


def _mhz(x: float) -> float:
    return x * 1e6


def _ghz(x: float) -> float:
    return x * 1e9


PRODUCT_BANDS: tuple[Band, ...] = (
    Band(
        key="ism_13p56",
        service="ISM",
        freq_hz=_mhz(13.56),
        opened_range="13.56 MHz (center; 13.553–13.567 MHz at ±0.05%)",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/"
            "part-18/subpart-C/section-18.301"
        ),
        citation="47 CFR § 18.301 (eCFR, opened 19 Nov 2026)",
        note=(
            "ISM center from the opened § 18.301 table. Below the FCC "
            "dielectric-calculator window (10–6000 MHz); inside the PMB "
            "1996 model range (10 Hz–100 GHz)."
        ),
    ),
    Band(
        key="ism_27p12",
        service="ISM",
        freq_hz=_mhz(27.12),
        opened_range="27.12 MHz (center; 26.957–27.283 MHz at ±0.6%)",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/"
            "part-18/subpart-C/section-18.301"
        ),
        citation="47 CFR § 18.301 (eCFR, opened 19 Nov 2026)",
        note=(
            "ISM center from the opened § 18.301 table. Lies inside the "
            "30–300 MHz range discussed as a lead (not a finding) in "
            "frequency-selection.md."
        ),
    ),
    Band(
        key="ism_40p68",
        service="ISM",
        freq_hz=_mhz(40.68),
        opened_range="40.68 MHz (center; 40.66–40.70 MHz at ±0.05%)",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/"
            "part-18/subpart-C/section-18.301"
        ),
        citation="47 CFR § 18.301 (eCFR, opened 19 Nov 2026)",
        note="ISM center from the opened § 18.301 table.",
    ),
    Band(
        key="cellular_ul",
        service="Cellular",
        freq_hz=_mhz(836.5),
        opened_range="824–849 MHz (mobile transmit / uplink span of Blocks A and B)",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/"
            "part-22/subpart-H/section-22.905"
        ),
        citation="47 CFR § 22.905 (eCFR, opened 19 Nov 2026)",
        note=(
            "Arithmetic midpoint of the opened 824–849 MHz span. Block A "
            "pairs 869–880 with 824–835 and 890–891.5 with 845–846.5 MHz; "
            "Block B pairs 880–890 with 835–845 and 891.5–894 with "
            "846.5–849 MHz."
        ),
    ),
    Band(
        key="cellular_dl",
        service="Cellular",
        freq_hz=_mhz(881.5),
        opened_range="869–894 MHz (base transmit / downlink span of Blocks A and B)",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/"
            "part-22/subpart-H/section-22.905"
        ),
        citation="47 CFR § 22.905 (eCFR, opened 19 Nov 2026)",
        note="Arithmetic midpoint of the opened 869–894 MHz span. See cellular_ul.",
    ),
    Band(
        key="ism_915",
        service="ISM / Part 15",
        freq_hz=_mhz(915.0),
        opened_range="915 MHz ISM center (±13 MHz); also 902–928 MHz in § 15.247",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/"
            "part-18/subpart-C/section-18.301"
        ),
        citation=(
            "47 CFR § 18.301 (eCFR) and 47 CFR § 15.247 (LII, opened 19 Nov 2026; "
            "https://www.law.cornell.edu/cfr/text/47/15.247)"
        ),
        note=(
            "ISM center from the opened § 18.301 table. § 15.247 (LII) is titled "
            "'Operation within the bands 902-928 MHz, 2400-2483.5 MHz, and "
            "5725-5850 MHz.'"
        ),
    ),
    Band(
        key="pcs_ul_block_b",
        service="Broadband PCS",
        freq_hz=_mhz(1877.5),
        opened_range="1870–1885 MHz (Block B, first of the paired ranges)",
        source_url="https://www.law.cornell.edu/cfr/text/47/24.229",
        citation="47 CFR § 24.229 (LII, opened 19 Nov 2026)",
        note=(
            "Arithmetic midpoint of opened Block B 1870–1885 MHz. The same "
            "opened section also lists Block A 1850–1865 MHz paired with "
            "1930–1945 MHz, and Block C 1895–1910 MHz paired with "
            "1975–1990 MHz. Later blocks on the page were not used because "
            "the extracted Block D text was truncated at '1865-18'."
        ),
    ),
    Band(
        key="pcs_dl_block_b",
        service="Broadband PCS",
        freq_hz=_mhz(1957.5),
        opened_range="1950–1965 MHz (Block B, paired range)",
        source_url="https://www.law.cornell.edu/cfr/text/47/24.229",
        citation="47 CFR § 24.229 (LII, opened 19 Nov 2026)",
        note="Arithmetic midpoint of opened Block B 1950–1965 MHz. See pcs_ul_block_b.",
    ),
    Band(
        key="wifi_2400",
        service="Wi-Fi / Part 15",
        freq_hz=_mhz(2441.75),
        opened_range="2400–2483.5 MHz",
        source_url="https://www.law.cornell.edu/cfr/text/47/15.247",
        citation="47 CFR § 15.247 (LII, opened 19 Nov 2026)",
        note=(
            "Arithmetic midpoint of the opened 2400–2483.5 MHz § 15.247 band. "
            "Nearby ISM center 2450 MHz is in § 18.301."
        ),
    ),
    Band(
        key="cbrs_3450",
        service="3.45 GHz Service",
        freq_hz=_mhz(3500.0),
        opened_range="3450–3550 MHz",
        source_url="https://www.law.cornell.edu/cfr/text/47/27.5",
        citation="47 CFR § 27.5(o) (LII, opened 19 Nov 2026)",
        note=(
            "Arithmetic midpoint of the opened 3450–3550 MHz '3.45 GHz Service' "
            "band in § 27.5(o)."
        ),
    ),
    Band(
        key="cband_3700",
        service="3.7 GHz Service",
        freq_hz=_mhz(3920.0),
        opened_range="3700–4140 MHz (Blocks A–E)",
        source_url="https://www.law.cornell.edu/cfr/text/47/27.5",
        citation="47 CFR § 27.5(m) (LII, opened 19 Nov 2026)",
        note=(
            "Arithmetic midpoint of the opened 3700–4140 MHz range. § 27.5(m) "
            "names Block A (3700–3800 MHz), B (3800–3900), C (3900–4000), "
            "D (4000–4100), and E (4100–4140)."
        ),
    ),
    Band(
        key="unii_5150",
        service="U-NII / Wi-Fi",
        freq_hz=_mhz(5200.0),
        opened_range="5.15–5.25 GHz",
        source_url="https://www.law.cornell.edu/cfr/text/47/15.407",
        citation="47 CFR § 15.407 (LII, opened 19 Nov 2026)",
        note=(
            "Arithmetic midpoint of the opened 5.15–5.25 GHz band in § 15.407. "
            "The same opened section also names 5.25–5.35 GHz, 5.47–5.725 GHz, "
            "5.725–5.850 GHz, 5.850–5.895 GHz, and 5.925–7.125 GHz."
        ),
    ),
    Band(
        key="ism_5800",
        service="ISM / U-NII",
        freq_hz=_mhz(5800.0),
        opened_range="5800 MHz ISM center (±75 MHz); 5.725–5.850 GHz in §§ 15.247 and 15.407",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/"
            "part-18/subpart-C/section-18.301"
        ),
        citation=(
            "47 CFR § 18.301 (eCFR); 47 CFR §§ 15.247 and 15.407 (LII, opened "
            "19 Nov 2026)"
        ),
        note="ISM center from the opened § 18.301 table, overlapping the 5.8 GHz U-NII / Part 15 band.",
    ),
    Band(
        key="unii_5925",
        service="U-NII / Wi-Fi 6E",
        freq_hz=_mhz(6525.0),
        opened_range="5.925–7.125 GHz",
        source_url="https://www.law.cornell.edu/cfr/text/47/15.407",
        citation="47 CFR § 15.407 (LII, opened 19 Nov 2026)",
        note=(
            "Arithmetic midpoint of the opened 5.925–7.125 GHz band. Above the "
            "FCC dielectric-calculator window (10–6000 MHz); inside the PMB "
            "1996 model range."
        ),
    ),
    Band(
        key="ism_24125",
        service="ISM",
        freq_hz=_ghz(24.125),
        opened_range="24.125 GHz (center; 24.000–24.250 GHz at ±125 MHz)",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/"
            "part-18/subpart-C/section-18.301"
        ),
        citation="47 CFR § 18.301 (eCFR, opened 19 Nov 2026)",
        note=(
            "ISM center from the opened § 18.301 table. Outside the FCC "
            "calculator window; inside the PMB 1996 model range."
        ),
    ),
    Band(
        key="umfus_27500",
        service="Upper Microwave Flexible Use (5G)",
        freq_hz=_ghz(27.925),
        opened_range="27.5–28.35 GHz",
        source_url="https://www.law.cornell.edu/cfr/text/47/30.4",
        citation="47 CFR § 30.4(c) (LII, opened 19 Nov 2026)",
        note=(
            "Arithmetic midpoint of the opened 27.5–28.35 GHz band. The same "
            "opened section also lists 24.25–24.45 GHz and 24.75–25.25 GHz, "
            "37–38.6 GHz, and 38.6–40 GHz."
        ),
    ),
    Band(
        key="umfus_38600",
        service="Upper Microwave Flexible Use (5G)",
        freq_hz=_ghz(39.3),
        opened_range="38.6–40 GHz",
        source_url="https://www.law.cornell.edu/cfr/text/47/30.4",
        citation="47 CFR § 30.4(d) (LII, opened 19 Nov 2026)",
        note="Arithmetic midpoint of the opened 38.6–40 GHz band in § 30.4(d).",
    ),
    Band(
        key="ism_61250",
        service="ISM",
        freq_hz=_ghz(61.25),
        opened_range="61.25 GHz (center; 61.000–61.500 GHz at ±250 MHz)",
        source_url=(
            "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/"
            "part-18/subpart-C/section-18.301"
        ),
        citation="47 CFR § 18.301 (eCFR, opened 19 Nov 2026)",
        note=(
            "ISM center from the opened § 18.301 table. Outside the FCC "
            "calculator window; inside the PMB 1996 model range. The same "
            "table also lists 122.50 GHz and 245.00 GHz, which exceed the "
            "100 GHz model range and are omitted here."
        ),
    ),
)
