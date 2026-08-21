"""
Rayleigh Analysis Entry Point
============================

Module
------
rayleigh.main

Description
-----------
Main entry point for all Rayleigh analysis workflows.

This module provides a unified interface for executing
different Rayleigh studies from a single application.

Available Analyses
------------------
single
    Perform a Rayleigh analysis on a single study.

comparison
    Compare multiple studies against a reference study.

Configuration
-------------
The analysis to run is selected through:

    rayleigh.config.ANALYSIS_TYPE

Examples
--------
Run a single-study analysis:

>>> ANALYSIS_TYPE = "single"

Run a comparison study:

>>> ANALYSIS_TYPE = "comparison"

Author
------
Lorenzo Zambelli

Version
-------
2.0.0
"""

from rayleigh.config import ANALYSIS_TYPE

#from rayleigh.analyses.single_study import (
 #   run_single_study,
#)

from rayleigh.analyses.run_comparison_study import (
    run_comparison_study,
)


# ============================================================
# AVAILABLE ANALYSES
# ============================================================

ANALYSES = {
    #"single": run_single_study,
    "comparison": run_comparison_study,
}


# ============================================================
# MAIN
# ============================================================

def main():
    """
    Execute the configured Rayleigh analysis.

    The analysis type is selected using
    ``ANALYSIS_TYPE`` in ``rayleigh.config``.

    Supported Analyses
    ------------------
    single
        Traditional Rayleigh analysis for a single study.

    comparison
        Multi-study Rayleigh comparison against a
        reference study.

    Raises
    ------
    ValueError
        Raised when an unknown analysis type is supplied.

    Returns
    -------
    None
    """

    try:
        runner = ANALYSES[ANALYSIS_TYPE]

    except KeyError:

        available = ", ".join(
            ANALYSES.keys()
        )

        raise ValueError(
            f"Unknown ANALYSIS_TYPE "
            f"'{ANALYSIS_TYPE}'. "
            f"Available analyses: {available}"
        )

    runner()


# ============================================================
# SCRIPT ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()