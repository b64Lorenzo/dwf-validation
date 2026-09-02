"""
Wave Height Map Analysis
========================

Module
------
waveheight.analyses.run

Description
-----------
Execute a wavefield analysis.

Workflow

Load simulation
    ↓
Load cache if available
    ↓
Process probes
    ↓
Compute Fourier components
    ↓
Generate plots
    ↓
Store results

Author
------
Lorenzo Zambelli
"""

from utils.io import load_all
from utils.logger import Logger

from waveheight.config import (
    SIMULATION_FOLDER,
    OUTPUT_DIR,
    CACHE_DIR,
    PLOTS,
)

from waveheight.processing.processor import (
    process_file,
)

from waveheight.plotting.plot2d import (
    plot_2d,
)


def run_waveheight_map():

    # =========================================================
    # LOGGER
    # =========================================================

    manager = Logger(
        name="waveheight",
        base_dir=str(OUTPUT_DIR),
        run_prefix="waveheight",
    )

    logger = manager.get_logger()

    logger.info("=" * 80)
    logger.info("STARTING WAVEHEIGHT ANALYSIS")
    logger.info("=" * 80)

    # =========================================================
    # CACHE
    # =========================================================

    cache_name = (
        SIMULATION_FOLDER.name
    )

    cache_file = (
        CACHE_DIR
        / f"{cache_name}.npy"
    )

    logger.info(
        "Simulation folder: %s",
        SIMULATION_FOLDER,
    )

    logger.info(
        "Cache file: %s",
        cache_file,
    )

    logger.info(
        "Using max_workers=1"
    )

    # =========================================================
    # LOAD DATA
    # =========================================================

    results = load_all(
        raw_csv_dirs=[
            SIMULATION_FOLDER
        ],
        cache_file=cache_file,
        process_file=process_file,
        logger=logger,
        max_workers=1,
    )

    logger.info(
        "Loaded %d records.",
        len(results),
    )

    if not results:

        logger.warning(
            "No data loaded."
        )

        return

    # =========================================================
    # PLOTS
    # =========================================================

    try:

        logger.info(
            "Generating plots..."
        )

        plot_2d(
            data=results,
            output_dir=manager.get_run_dir(),
            logger=logger,
            plots=PLOTS,
        )

        logger.info(
            "Successfully generated plots."
        )

    except Exception as exc:

        logger.exception(
            "Failed generating plots. "
            "Error: %s",
            exc,
        )

    logger.info("=" * 80)
    logger.info("WAVEHEIGHT ANALYSIS FINISHED")
    logger.info("=" * 80)