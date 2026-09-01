"""
Multi-Study Rayleigh Comparison
===============================

Module
------
rayleigh.analyses.comparison_study

Description
-----------
Execute and orchestrate a Rayleigh comparison study.

This workflow:

1. Loads all configured studies.
2. Applies configured filters.
3. Groups results.
4. Generates comparison figures.
5. Stores results in a timestamped run directory.

Author
------
Lorenzo Zambelli

Version
-------
2.1.0
"""

from utils.io import load_all
from utils.logger import Logger

from rayleigh.config import (
    CACHE_DIR,
    COMPARISON_STUDY,
    FILTER_SETS,
    GROUP_BY_LIST,
    DT_MODE,
    TIME_WINDOW,
    PLOTS
)

from rayleigh.processing.processor import process_file

from rayleigh.processing.grouping import collect

from rayleigh.plotting.comparison_plot import (
    plot_comparison,
)


def run_comparison_study():
    """
    Execute a multi-study Rayleigh comparison.

    Returns
    -------
    None

    Notes
    -----
    Workflow

    Load studies
        ↓
    Apply filters
        ↓
    Group data
        ↓
    Generate plots
        ↓
    Save outputs
    """

    # =========================================================
    # LOGGER
    # =========================================================

    output_dir = COMPARISON_STUDY["output_dir"]

    manager = Logger(
        name="rayleigh_comparison",
        base_dir=str(output_dir),
        run_prefix="rayleigh_comparison",
    )

    logger = manager.get_logger()

    logger.info("=" * 80)
    logger.info("STARTING RAYLEIGH COMPARISON STUDY")
    logger.info("=" * 80)

    logger.info(
        "Reference study: %s",
        COMPARISON_STUDY["reference_study"],
    )

    logger.info(
        "Configured studies: %d",
        len(COMPARISON_STUDY["studies"]),
    )

    for study in COMPARISON_STUDY["studies"]:
        logger.debug(
            "Configured study: %s",
            study,
        )

    # =========================================================
    # LOAD ALL STUDIES
    # =========================================================

    logger.info(
        "Loading study data..."
    )

    all_results = []

    for study_name, entries in COMPARISON_STUDY["studies"].items():

        logger.info(
            "Loading study: %s",
            study_name,
        )

        for folder, cache_name in entries:

            cache_file = (
                CACHE_DIR /
                f"{cache_name}.npy"
            )

            logger.debug(
                "Folder: %s",
                folder,
            )

            logger.debug(
                "Cache: %s",
                cache_file,
            )

            study_results = load_all(
                raw_csv_dirs=[folder],
                cache_file=cache_file,
                process_file=process_file,
                logger=logger,
                max_workers=8,
            )

            logger.info(
                "Loaded %d records for %s",
                len(study_results),
                study_name,
            )

            for meta, wave, m0 in study_results:

                all_results.append(
                    (
                        study_name,
                        meta,
                        wave,
                        m0,
                    )
                )

    logger.info(
        "Total loaded records: %d",
        len(all_results),
    )

    if not all_results:

        logger.warning(
            "No data was loaded. Stopping analysis."
        )

        return

    # =========================================================
    # FILTER LOOP
    # =========================================================

    for filters in FILTER_SETS:

        logger.info("-" * 80)

        logger.info(
            "Filter set: %s",
            filters,
        )

        # =====================================================
        # GROUP LOOP
        # =====================================================

        for group_by in GROUP_BY_LIST:

            logger.info(
                "Grouping by: %s",
                group_by,
            )

            groups = collect(
                data=all_results,
                filters=filters,
                group_by=group_by,
                dt_mode=DT_MODE,
                include_study=True,
            )

            logger.debug(
                "Generated %d groups",
                len(groups),
            )

            if not groups:

                logger.warning(
                    "No groups generated for %s",
                    group_by,
                )

                continue

            logger.info(
                "Generating comparison figure..."
            )

            try:

                plot_comparison(
                    groups=groups,
                    group_by=group_by,
                    filters=filters,
                    output_dir=manager.get_run_dir(),
                    study_names=list(
                        COMPARISON_STUDY["studies"].keys()
                    ),
                    reference_study=(
                        COMPARISON_STUDY[
                            "reference_study"
                        ]
                    ),
                    space_shift=(
                        COMPARISON_STUDY[
                            "space_shift"
                        ]
                    ),
                    dt_mode=DT_MODE,
                    time_window=TIME_WINDOW,
                    logger=logger,
                    plots=PLOTS,
                )

                logger.info(
                    "Successfully generated plot for %s",
                    group_by,
                )

            except Exception as exc:

                logger.exception(
                    "Failed generating plot for "
                    "%s. Error: %s",
                    group_by,
                    exc,
                )

    logger.info("=" * 80)
    logger.info("COMPARISON STUDY FINISHED")
    logger.info("=" * 80)