"""
Wave Height Grid Analysis

Author
------
Lorenzo Zambelli
"""

from waveheight.config import ANALYSIS_TYPE

from waveheight.analyses.run import (
    run_waveheight_map,
)

ANALYSES = {
    "waveheight_map": run_waveheight_map,
}


def main():

    try:
        runner = ANALYSES[ANALYSIS_TYPE]

    except KeyError:

        available = ", ".join(ANALYSES.keys())

        raise ValueError(
            f"Unknown ANALYSIS_TYPE '{ANALYSIS_TYPE}'. "
            f"Available analyses: {available}"
        )

    runner()


if __name__ == "__main__":
    main()