"""
Rayleigh Analysis Configuration
===============================

Module
------
rayleigh.config

Description
-----------
Central configuration file for all Rayleigh analysis workflows.

This file should be the primary user-editable file within
the Rayleigh project.

Supported analysis modes
------------------------
single
    Perform a traditional Rayleigh analysis on a single study.

comparison
    Compare multiple studies against a reference study.

Configuration Sections
----------------------
ANALYSIS
    Select which analysis workflow to execute.

SINGLE_STUDY
    Configuration used by the single-study workflow.

COMPARISON_STUDY
    Configuration used by the multi-study comparison workflow.

SHARED SETTINGS
    Settings used by all workflows.

Author
------
Lorenzo Zambelli

Version
-------
2.0.0
"""

from pathlib import Path
import re

# ============================================================
# ANALYSIS SELECTION
# ============================================================

ANALYSIS_TYPE = "comparison"

# Available options
#
# "single"
# "comparison"

# ============================================================
# SINGLE STUDY CONFIGURATION
# ============================================================

SINGLE_STUDY = {

    "name": "DWF Captive",

    "raw_csv_dirs": [
        Path(
            r"H:\Documents\validation\data\LNGC\Results"
            r"\xsims\DWFfixed\DWFdz0.1fixed"
        ),
    ],

    "output_dir": Path(
        r"H:\Documents\validation\data\LNGC\Results"
        r"\xsims\DWFfixed\DWFdz0.1fixed\plots\dx2.5"
    ),

    "cache_file": Path(
        r"H:\Documents\validation\data\LNGC\Results"
        r"\xsims\cache\dwf_dz0.1.npy"
    ),
}

SINGLE_STUDY["output_dir"].mkdir(
    parents=True,
    exist_ok=True,
)

# ============================================================
# MULTI-STUDY CONFIGURATION
# ============================================================

COMPARISON_STUDY = {

    "reference_study": "DWF-dx2.5m",

    "studies": {

    "DWF-dw15": [
        (Path(r"H:\Documents\validation\data\LNGC\Results\xsims\DWFspring\dx2.5\dz0.1"),
         "dwf_fixed_dx2.5dz0.1dw0.05dtheta15_interpangle"),
    ],

    "DWF-dw10m": [
        (Path(r"H:\Documents\validation\data\LNGC\Results\xsims\DWFInterpAngle\dx2.5\dz0.1dw0.05dtheta10"),
         "dwf_fixed_dx2.5dz0.1dw0.05dtheta10_interpangle"),
    ],

    "DWF-dx2.5m": [
        (Path(r"H:\Documents\validation\data\LNGC\Results\xsims\DWFspring\dx2.5\dz0.1"),
         "dwf_fixed_dx2.5dz0.1dw0.05theta15"),
    ],

        # Example additional study
        #
        # "DWF-dz5m": [
        #     (
        #         Path(
        #             r"H:\Documents\validation\data"
        #             r"\LNGC\Results\xsims"
        #             r"\DWFspring\dx2.5\dz0.1"
        #         ),
        #         "dwf_spring_dx5",
        #     ),
        # ],

    },

    "output_dir": Path(
        r"H:\Documents\validation\data\LNGC\Results"
        r"\analysis\DWF_interpanglefixed"
    ),

    "space_shift": {

        "DWF": 0.0,

        "DWF-dy0.5m": 0.5,

        "DWF-dy1m": 1.0,

        "DWF-dy1.25m": 1.25,

        "DWF-dy2m": 2.0,
    },
}

COMPARISON_STUDY["output_dir"].mkdir(
    parents=True,
    exist_ok=True,
)

# ============================================================
# SHARED CACHE SETTINGS
# ============================================================

CACHE_DIR = Path(
    r"H:\Documents\validation\data"
    r"\LNGC\Results\xsims\cache"
)

CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# ============================================================
# TIME SETTINGS
# ============================================================

TIME_WINDOW = (
    None,
    None,
)

# Examples
#
# (None, None)
# (100, None)
# (100, 600)

# ============================================================
# DT TRANSFORMATION MODE
# ============================================================

DT_MODE = "ppp"

# Available modes
#
# "raw"
# "order"
# "ppp"

# ============================================================
# PLOTTING SETTINGS
## ==========================================================
# comparison: plot comparison of multiple studies
# distributions: plot distributions of a single study
# 95ci: plot 95% confidence intervals of a single study

PLOTS = ["95ci"]

# ============================================================
# GROUPING DEFINITIONS
# ============================================================

GROUP_BY_LIST = [

    #["dt"],
    #["dt", "dx"],

    #["dx"],

    #["pos"],
    #["pos", "dt"],

    ["angle"],
    ["angle", "pos"],
    

    ["depth"],
    #["depth", "dt"],

    ["freq"],
   # ["freq", "dt"],

]

# Example alternative sets
#
# GROUP_BY_LIST = [["freq"]]
#
# GROUP_BY_LIST = [["depth"]]
#
# GROUP_BY_LIST = [["pos"]]
#
# GROUP_BY_LIST = [["angle"]]

# ============================================================
# FILTER SETTINGS
# ============================================================

DX_FILTER = (None, None)

FREQ_BANDS = [
    (0.2, 0.8),     # long waves
    (0.8, 1.6),     # intermediate waves
    (1.6, None),    # short waves
    (None, None),   # all waves
]

# DX_FILTER = (None, None)
FILTER_SETS =  ([

    {
        "freq": freq,
        "angle": (30, 90),
        "dt": (None, None),
        "dx": DX_FILTER,
        "pan": (None, None),
        "depth": (22.5, 50),
        "pos": None,
    }

    for freq in FREQ_BANDS
    #for angle in range(45, 91, 15)

]
    #             + [
    #
    # {
    #     "freq": (None, None),
    #     "angle": (30, 150),
    #     "dt": (None, None),
    #     "dx": DX_FILTER,
    #     "pan": (None, None),
    #     "depth": (22.5, 50),
    #     "pos": None,
    # },
    #
    # {
    #     "freq": (None, None),
    #     "angle": (30, 90),
    #     "dt": (None, None),
    #     "dx": DX_FILTER,
    #     "pan": (None, None),
    #     "depth": (22.5, 50),
    #     "pos": None,
    # },
    #
    # {
    #     "freq": (None, None),
    #     "angle": (90, 150),
    #     "dt": (None, None),
    #     "dx": DX_FILTER,
    #     "pan": (None, None),
    #     "depth": (22.5, 50),
    #     "pos": None,
    # },
    #]
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
# PLOTTING LABELS
# ============================================================

XLABELS = {

    "freq": r"Angular frequency $\omega$ [rad/s]",

    "depth": r"$Y$ [m]",

    "angle": "Angle [deg]",

    "pos": (
        "Position X [m] "
        "w.r.t Hydrodynamic center"
    ),

    "dx": "dx [m]",

    "pan": "Panel ID",
}