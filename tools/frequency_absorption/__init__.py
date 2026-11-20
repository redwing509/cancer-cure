"""Frequency-versus-absorption comparison (first-order, published parameters).

MIT License. This is not medical advice and is not a regulatory determination.
It cannot, by itself, prove why a product band was chosen or that a frequency
is "safer."
"""

from .cole_cole import TISSUES, complex_relative_permittivity, effective_conductivity
from .plane_wave import skin_depth, plane_wave_estimates
from .bands import PRODUCT_BANDS

__all__ = [
    "TISSUES",
    "PRODUCT_BANDS",
    "complex_relative_permittivity",
    "effective_conductivity",
    "skin_depth",
    "plane_wave_estimates",
]
