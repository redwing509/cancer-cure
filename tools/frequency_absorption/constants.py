"""Physical constants copied from opened official sources.

vacuum electric permittivity ε0
    NIST 2022 CODATA recommended value, opened 19 Nov 2026 (Pacific Time):
    "Numerical value  8.854 187 8188 x 10-12 F m-1"
    Source: https://physics.nist.gov/cgi-bin/cuu/Value?ep0

speed of light in vacuum c
    Exact SI value, 299 792 458 m s^{-1}. Used with ε0 to obtain μ0 = 1/(ε0 c^2)
    so that the plane-wave impedance is consistent with the opened ε0.

mass-density convention ρ0
    1000 kg m^{-3} is used only to put a specific-absorption-rate *estimate*
    into W kg^{-1}. Gabriel et al. (1996), Table 1, does not report mass
    density. This is a conventional water-like density, not a measured tissue
    density, and is labeled as such in every output column.
"""

# NIST 2022 CODATA vacuum electric permittivity, F m^{-1}.
# https://physics.nist.gov/cgi-bin/cuu/Value?ep0
# Quote opened 19 Nov 2026: "Numerical value  8.854 187 8188 x 10-12 F m-1"
EPSILON_0 = 8.8541878188e-12

# Exact SI speed of light, m s^{-1}.
SPEED_OF_LIGHT = 299_792_458.0

# Magnetic constant implied by the opened ε0 and exact c: μ0 = 1/(ε0 c^2).
MU_0 = 1.0 / (EPSILON_0 * SPEED_OF_LIGHT * SPEED_OF_LIGHT)

# Conventional density for the SAR *estimate* only, kg m^{-3}. Not from Gabriel 1996.
RHO_CONVENTIONAL_KG_M3 = 1000.0

# Incident power density used to normalize estimates, W m^{-2}.
# Results scale linearly with this value.
S0_W_M2 = 1.0
