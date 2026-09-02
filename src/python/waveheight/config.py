"""
Wave Height Grid Configuration
==============================

Author
------
Lorenzo Zambelli
"""

from pathlib import Path
import re

# ============================================================
# ANALYSIS
# ============================================================

ANALYSIS_TYPE = "waveheight_map"

# ============================================================
# INPUT
# ============================================================

sim = "angle30_dx1_dt0.031416_freq2_beam0_pan3000"

SIMULATION_FOLDER = (
    Path(
        r"H:\Documents\validation\src\xsimulation_202502"
        r"\simulations\anysim"
        r"\dz0.1dw0.1dtheta30fixedAngle30"
    )
    / sim
)

# ============================================================
# OUTPUT
# ============================================================

OUTPUT_DIR = (

Path(

r"H:\Documents\validation\data\plots\waveheight_grid"

)

/ sim

)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# ============================================================
# CACHE
# ============================================================

CACHE_DIR = Path(
    r"H:\Documents\validation\data"
    r"\cache\waveheight"
)

CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

CACHE_FILE = (
    CACHE_DIR
    / f"{sim}.npy"
)

# ============================================================
# METADATA EXTRACTION
# ============================================================

FOLDER_RE = re.compile(
    r"angle(?P<angle>\d+)"
    r"_dx(?P<dx>[0-9.]+)"
    r"_dt(?P<dt>[0-9.]+)"
    r"_freq(?P<freq>[0-9.]+)"
    r".*_pan(?P<pan>\d+)"
)

# ============================================================
# FOURIER
# ============================================================

TRANSIENT_TIME = 0.0

TIME_WINDOW = (
    None,
    None,
)

# ============================================================
# PLOTS
# ============================================================

PLOTS = [

    "real",

    "imag",

    "abs",

    "phase",

]

# ============================================================
# LABELS
# ============================================================

XLABELS = {

    "xPos":
        r"$x$ [m]",

    "yPos":
        r"$y$ [m]",

    "real":
        r"$Re(\hat{\eta})$ [m]",

    "imag":
        r"$Im(\hat{\eta})$ [m]",

    "abs":
        r"$|\hat{\eta}|$ [m]",

    "phase":
        r"Phase [rad]",

}

# ============================================================
# COLORMAPS
# ============================================================

# ============================================================
# COLORMAPS
# ============================================================

COLORMAPS = {

    #
    # Negative -> Blue
    # Zero     -> White
    # Positive -> Red
    #
    "real":
        "RdBu_r",

    "imag":
        "RdBu_r",

    #
    # Low      -> Blue
    # Medium   -> Purple
    # High     -> Yellow
    #
    "abs":
        "plasma",

    #
    # Cyclic phase map
    #
    "phase":
        "twilight",

}