"""
Rayleigh Comparison Plotting
===========================

Module
------
rayleigh.plotting.comparison_plot

Description
-----------
Create comparison plots for multiple studies.

The generated figure contains:

1. Rayleigh PDF comparison
2. Exceedance comparison
3. Mean and standard deviation comparison
4. Percentage difference relative to a reference study

Author
------
Lorenzo Zambelli

Version
-------
2.0.0
"""

import matplotlib
matplotlib.use("Agg")

from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.stats import bootstrap
import numpy as np

from matplotlib.lines import Line2D

from utils.statistics import exceedance
from utils.utils import (
    sort_key,
    fmt,
    format_time_window
)

from utils.filters import (
    format_filters,
)

from utils.positions import (
    pos_to_order,
    pos_to_label,
    get_xlabel,
)


def relative_error_statistic(
    ref_sample,
    study_sample,
):
    ref_mean = np.mean(ref_sample)

    study_mean = np.mean(study_sample)

    return (
        100.0
        * (study_mean - ref_mean)
        / ref_mean
    )
    
    
def bca_worker(args):

    key, ref_wave, study_wave = args

    err, ci_low, ci_high = (
        bootstrap_relative_error_bca(
            ref_wave,
            study_wave,
            confidence_level=0.95,
            n_resamples=1000,
        )
    )

    return (
        key,
        err,
        ci_low,
        ci_high,
    )
    
def difference_statistic(
    ref_sample,
    study_sample,
):
    return (
        np.mean(study_sample)
        -
        np.mean(ref_sample)
    )
    
    
def bootstrap_relative_error_bca(
    ref_wave,
    study_wave,
    confidence_level=0.95,
    n_resamples=1000,
    max_samples=10000,
):
    """
    Relative error with BCa confidence interval.

    To avoid excessive memory usage, very large wave
    distributions are randomly subsampled before
    performing the bootstrap.

    Parameters
    ----------
    ref_wave : array-like
        Reference wave heights.

    study_wave : array-like
        Study wave heights.

    confidence_level : float
        Confidence level.

    n_resamples : int
        Number of bootstrap resamples.

    max_samples : int
        Maximum samples used for BCa bootstrap.

    Returns
    -------
    error : float

    ci_low : float

    ci_high : float
    """

    ref_wave = np.asarray(ref_wave)
    study_wave = np.asarray(study_wave)

    # --------------------------------------------
    # SUBSAMPLE VERY LARGE DATASETS
    # --------------------------------------------

    if len(ref_wave) > max_samples:

        ref_wave = np.random.choice(
            ref_wave,
            size=max_samples,
            replace=False,
        )

    if len(study_wave) > max_samples:

        study_wave = np.random.choice(
            study_wave,
            size=max_samples,
            replace=False,
        )

    # --------------------------------------------
    # SAFETY CHECKS
    # --------------------------------------------

    if len(ref_wave) < 10:
        raise ValueError(
            f"Reference sample too small ({len(ref_wave)})"
        )

    if len(study_wave) < 10:
        raise ValueError(
            f"Study sample too small ({len(study_wave)})"
        )

    if np.mean(ref_wave) == 0:
        raise ValueError(
            "Reference mean is zero."
        )

    # --------------------------------------------
    # CENTRAL ESTIMATE
    # --------------------------------------------

    error = (
        100.0
        * (
            np.mean(study_wave)
            - np.mean(ref_wave)
        )
        / np.mean(ref_wave)
    )

    # --------------------------------------------
    # BCa BOOTSTRAP
    # --------------------------------------------

    result = bootstrap(
        (
            ref_wave,
            study_wave,
        ),
        relative_error_statistic,
        paired=False,
        vectorized=False,
        confidence_level=confidence_level,
        n_resamples=n_resamples,
        method="percentile",
    )

    return (
        error,
        float(result.confidence_interval.low),
        float(result.confidence_interval.high),
    )

def plot_comparison(
    groups,
    group_by,
    filters,
    output_dir,
    study_names,
    reference_study,
    space_shift,
    dt_mode,
    time_window,
    logger,
):
    """
    Create a comparison figure for multiple studies.

    Parameters
    ----------
    groups : dict
        Output from grouping.collect().

    group_by : list[str]
        Active grouping keys.

    filters : dict
        Filter definition.

    output_dir : Path
        Output directory.

    study_names : list[str]
        Names of all studies.

    reference_study : str
        Study used as comparison baseline.

    space_shift : dict
        Optional shift applied to depth studies.

    dt_mode : str
        dt transformation mode.

    time_window : tuple
        Active time window.
    """

    fig = plt.figure(figsize=(26, 14))

    gs = fig.add_gridspec(
        2,
        2,
        height_ratios=[1, 1.2]
    )

    ax_pdf = fig.add_subplot(gs[0, 0])
    ax_exc = fig.add_subplot(gs[0, 1])

    ax_stat = fig.add_subplot(gs[1, :])
    ax_stat2 = ax_stat.twinx()

    linestyles = ["-", "--", ":", "-."]

    # ====================================================
    # SORT GROUPS
    # ====================================================

    sorted_groups = sorted(
        groups.items(),
        key=lambda x: sort_key((x[0][1:],))
    )

    studies = sorted({
        g[0]
        for g, _ in sorted_groups
    })

    g_vals = [
        g[1:]
        for g, _ in sorted_groups
    ]

    g1_vals = sorted({
        g[0]
        for g in g_vals
    })

    # ====================================================
    # COLORMAP
    # ====================================================

    is_numeric = all(
        isinstance(v, (int, float))
        for v in g1_vals
        if v is not None
    )

    if is_numeric:

        norm = mcolors.Normalize(
            vmin=min(g1_vals),
            vmax=max(g1_vals),
        )

        cmap = matplotlib.colormaps["turbo"]

        color_map = {
            v: cmap(norm(v))
            for v in g1_vals
        }

    else:

        cmap = matplotlib.colormaps["tab10"]

        color_map = {
            v: cmap(i % 10)
            for i, v in enumerate(g1_vals)
        }

    # ====================================================
    # STUDY STYLE
    # ====================================================

    study_ls = {
        s: linestyles[i % len(linestyles)]
        for i, s in enumerate(studies)
    }

    # ====================================================
    # STORAGE
    # ====================================================

    stats = {
        s: {}
        for s in studies
    }

    # ====================================================
    # TOP FIGURES
    # ====================================================

    for full_key, data in sorted_groups:

        study = full_key[0]
        key = full_key[1:]

        wave = np.abs(data["wave"])
        m0 = data["m0"]

        color = color_map[key[0]]
        ls = study_ls[study]

        scale = np.sqrt(8 * m0)

        x = np.linspace(
            0,
            3 * scale,
            400,
        )

        pdf = (
            x / (4 * m0)
        ) * np.exp(
            -x**2 / (8 * m0)
        )

        ax_pdf.plot(
            x,
            pdf,
            color=color,
            linestyle=ls,
        )

        xw, pw = exceedance(wave)

        ax_exc.plot(
            xw,
            pw,
            color=color,
            linestyle=ls,
        )

        stats[study][key] = {

            "mean": np.mean(wave),

            "std": np.std(wave),

            "wave": wave,

        }

    # ====================================================
    # BOTTOM PLOT
    # ====================================================

    cmap2 = plt.get_cmap("tab10")

    study_colors = {
        s: cmap2(i)
        for i, s in enumerate(studies)
    }

    ref_data = stats.get(
        reference_study,
        {},
    )

    for study in studies:

        data = stats[study]

        keys = sorted(data.keys())

        if not keys:
            continue

        if group_by[0] == "pos":

            keys = sorted(
                keys,
                key=lambda k: pos_to_order(k[0])
            )

            x_vals = np.arange(len(keys))

            labels = []

            for k in keys:

                if k[0] == "HC":

                    labels.append(
                        r"$x_{HC}$"
                        "\n(135.934 m)"
                    )

                else:

                    labels.append(
                        pos_to_label(k[0])
                    )

        elif group_by[0] == "depth":

            shift = space_shift.get(
                study,
                0.0,
            )

            x_vals = np.array([
                k[0] + shift
                for k in keys
            ])

            labels = None

        else:

            x_vals = np.array([
                k[0]
                for k in keys
            ])

            labels = None

        mean_vals = np.array([
            data[k]["mean"]
            for k in keys
        ])

        std_vals = np.array([
            data[k]["std"]
            for k in keys
        ])

        c = study_colors[study]

        ax_stat.plot(
            x_vals,
            mean_vals,
            color=c,
            marker="o",
            linestyle="-",
        )

        ax_stat.plot(
            x_vals,
            std_vals,
            color=c,
            linestyle="--",
        )

        # ============================================
        # DIFFERENCE TO REFERENCE
        # ============================================

        if (
            study != reference_study
            and ref_data
        ):
            # --- build reference arrays
            ref_keys = sorted(ref_data.keys())

            if group_by[0] == "pos":
                ref_keys = sorted(
                    ref_keys,
                    key=lambda k: pos_to_order(k[0])
                )

                x_ref = np.arange(len(ref_keys))

            else:
                x_ref = np.array(
                    [k[0] for k in ref_keys]
                )

            y_ref = np.array([
                ref_data[k]["mean"]
                for k in ref_keys
            ])

            # --- build current arrays
            cur_keys = sorted(data.keys())

            if group_by[0] == "pos":

                cur_keys = sorted(
                    cur_keys,
                    key=lambda k: pos_to_order(k[0])
                )

                x_cur = np.arange(
                    len(cur_keys)
                )

            elif group_by[0] == "depth":

                shift = space_shift.get(
                    study,
                    0.0,
                )

                x_cur = np.array(
                    [
                        k[0] + shift
                        for k in cur_keys
                    ]
                )

            else:

                x_cur = np.array(
                    [
                        k[0]
                        for k in cur_keys
                    ]
                )

            y_cur = np.array(
                [
                    data[k]["mean"]
                    for k in cur_keys
                ]
            )

            xmin = max(
                np.min(x_ref),
                np.min(x_cur),
            )

            xmax = min(
                np.max(x_ref),
                np.max(x_cur),
            )

            if xmin < xmax:

                x_common = np.linspace(
                    xmin,
                    xmax,
                    200,
                )

                y_ref_i = np.interp(
                    x_common,
                    x_ref,
                    y_ref,
                )

                y_cur_i = np.interp(
                    x_common,
                    x_cur,
                    y_cur,
                )

                with np.errstate(
                    divide="ignore",
                    invalid="ignore",
                ):

                    diff = (
                        100.0
                        * (y_cur_i - y_ref_i)
                        / y_ref_i
                    )

                ax_stat2.plot(
                    x_common,
                    diff,
                    color=study_colors[study],
                    linewidth=2,
                    alpha=0.9,
                )

        if labels is not None:

            ax_stat.set_xticks(x_vals)
            ax_stat.set_xticklabels(labels)

    # ====================================================
    # FORMATTING
    # ====================================================

    ax_pdf.set_title("Rayleigh PDF")
    ax_pdf.set_xlabel("H [m]")
    ax_pdf.set_ylabel("f(H)")
    ax_pdf.grid()

    ax_exc.set_title("Exceedance")
    ax_exc.set_xlabel("H [m]")
    ax_exc.set_ylabel("P(H > h)")
    ax_exc.grid()

    ax_stat.set_title("Mean & Std")
    ax_stat.set_xlabel(
        get_xlabel(group_by[0])
    )
    ax_stat.set_ylabel("H [m]")
    ax_stat.grid()

    ax_stat2.set_ylabel("% Difference")
    ax_stat2.axhline(
        0,
        color="black",
        linestyle=":",
    )

    title = (
        f"{' vs '.join(study_names)} | "
        f"Group by: {group_by} | "
        f"{format_filters(filters)}"
    )
    
    # ====================================================
    # LEGENDS
    # ====================================================

    legend_x = 0.92
    y_shift = 0.45

    # ----------------------------------------------------
    # GROUP LEGEND / COLORBAR
    # ----------------------------------------------------

    if is_numeric:

        bbox_pdf = ax_pdf.get_position()
        bbox_exc = ax_exc.get_position()

        y0 = min(
            bbox_pdf.y0,
            bbox_exc.y0,
        )

        y1 = max(
            bbox_pdf.y1,
            bbox_exc.y1,
        )

        cax = fig.add_axes(
            [
                0.92,
                y0,
                0.015,
                y1 - y0,
            ]
        )

        sm = plt.cm.ScalarMappable(
            cmap=cmap,
            norm=norm,
        )

        sm.set_array([])

        cbar = fig.colorbar(
            sm,
            cax=cax,
        )

        cbar.set_label(
            group_by[0]
        )

        fig.subplots_adjust(
            left=0.06,
            right=0.90,
            top=0.92,
            bottom=0.08,
            wspace=0.15,
        )

    else:

        legend_group = [

            Line2D(
                [0],
                [0],
                color=color_map[v],
                lw=3,
                label=f"{group_by[0]} = {v}",
            )

            for v in g1_vals
        ]

        fig.legend(
            handles=legend_group,
            bbox_to_anchor=(legend_x, 0.90),
            loc="upper left",
            title=group_by[0],
            fontsize=8,
            ncol=1,
        )

    # ----------------------------------------------------
    # STUDY LINESTYLE
    # ----------------------------------------------------

    fig.legend(
        handles=[
            Line2D(
                [0],
                [0],
                color="black",
                linestyle=study_ls[s],
                lw=3,
                label=s,
            )
            for s in studies
        ],
        bbox_to_anchor=(
            0.92,
            0.98,
        ),
        loc="upper left",
        title="Study (linestyle)",
    )

    # ----------------------------------------------------
    # STUDY COLOR
    # ----------------------------------------------------

    fig.legend(
        handles=[
            Line2D(
                [0],
                [0],
                color=study_colors[s],
                lw=3,
                label=s,
            )
            for s in studies
        ],
        bbox_to_anchor=(
            legend_x,
            0.98 - y_shift - 0.10,
        ),
        loc="upper left",
        title="Study (color)",
    )

    # ----------------------------------------------------
    # STATISTICS
    # ----------------------------------------------------

    fig.legend(
        handles=[
            Line2D(
                [0],
                [0],
                color="black",
                linestyle="-",
                marker="o",
                label="Mean",
            ),
            Line2D(
                [0],
                [0],
                color="black",
                linestyle="--",
                label="Std",
            ),
        ],
        bbox_to_anchor=(
            legend_x,
            0.98 - y_shift - 0.20,
        ),
        loc="upper left",
        title="Statistics",
    )

    # ----------------------------------------------------
    # DIFFERENCE
    # ----------------------------------------------------

    fig.legend(
        handles=[
            Line2D(
                [0], [0],
                color=study_colors[s],
                linestyle="-",
                linewidth=2,
                label=f"{s} %Diff"
            )
            for s in studies
            if s != reference_study
        ],
        bbox_to_anchor=(
            legend_x,
            0.98 - y_shift - 0.30,
        ),
        loc="upper left",
        title=f"% Difference vs {reference_study}",
    )

    fig.subplots_adjust(
        left=0.08,
        right=0.89,
        top=0.90,
        bottom=0.08,
    )

    fig.suptitle(
        title,
        fontsize=16,
    )
    
    

    filename = (
        f"compare_"
        f"{'-'.join(group_by)}_"
        f"{dt_mode}_"
        f"{format_filters(filters)}_"
        f"{format_time_window(time_window)}"
        f".png"
    )

    fig.savefig(
        output_dir / filename,
        dpi=200,
        bbox_inches="tight",
    )

    plt.close(fig)
    
    
    
    
    
        # ====================================================
    # NEW FIGURE : TOP PANELS ONLY
    # ====================================================

    fig_top, (ax_pdf2, ax_exc2) = plt.subplots(
        1,
        2,
        figsize=(20, 8)
    )

    for full_key, data in sorted_groups:

        study = full_key[0]
        key = full_key[1:]

        wave = np.abs(data["wave"])
        m0 = data["m0"]

        color = color_map[key[0]]
        ls = study_ls[study]

        scale = np.sqrt(8 * m0)

        x = np.linspace(
            0,
            3 * scale,
            400,
        )

        pdf = (
            x / (4 * m0)
        ) * np.exp(
            -x**2 / (8 * m0)
        )

        ax_pdf2.plot(
            x,
            pdf,
            color=color,
            linestyle=ls,
        )

        xw, pw = exceedance(wave)

        ax_exc2.plot(
            xw,
            pw,
            color=color,
            linestyle=ls,
        )

    # ----------------------------------------------------
    # FORMATTING
    # ----------------------------------------------------

    ax_pdf2.set_title("Rayleigh PDF")
    ax_pdf2.set_xlabel("H [m]")
    ax_pdf2.set_ylabel("f(H)")
    ax_pdf2.grid()

    ax_exc2.set_title("Exceedance")
    ax_exc2.set_xlabel("H [m]")
    ax_exc2.set_ylabel("P(H > h)")
    ax_exc2.grid()

        # ----------------------------------------------------
    # STUDY LEGEND (LINESTYLE)
    # ----------------------------------------------------

    fig_top.legend(
        handles=[
            Line2D(
                [0],
                [0],
                color="black",
                linestyle=study_ls[s],
                lw=3,
                label=s,
            )
            for s in studies
        ],
        loc="upper center",
        bbox_to_anchor=(0.50, 0.93),
        ncol=len(studies),
        title="Study (linestyle)",
        frameon=True,
    )

    # ----------------------------------------------------
    # POSITION LEGEND (COLOR)
    # ----------------------------------------------------

    if is_numeric:

        cax = fig_top.add_axes(
            [0.92, 0.15, 0.02, 0.70]
        )

        sm = plt.cm.ScalarMappable(
            cmap=cmap,
            norm=norm,
        )

        sm.set_array([])

        cbar = fig_top.colorbar(
            sm,
            cax=cax,
        )

        cbar.set_label(
            group_by[0]
        )

    else:

        legend_group = [
            Line2D(
                [0],
                [0],
                color=color_map[v],
                lw=3,
                label=f"{v}",
            )
            for v in g1_vals
        ]

        fig_top.legend(
            handles=legend_group,
            loc="lower center",
            bbox_to_anchor=(0.50, 0.00),
            ncol=min(6, len(g1_vals)),
            title=f"{group_by[0]} (color)",
            frameon=True,
        )

    fig_top.subplots_adjust(
        left=0.08,
        right=0.90,
        top=0.85,
        bottom=0.12,
        wspace=0.25,
    )

    fig_top.subplots_adjust(
        left=0.08,
        right=0.90,
        top=0.88,
        bottom=0.10,
        wspace=0.25,
    )

    fig_top.suptitle(
        title,
        fontsize=16,
    )

    top_filename = (
        f"compare_top_"
        f"{'-'.join(group_by)}_"
        f"{dt_mode}_"
        f"{format_filters(filters)}_"
        f"{format_time_window(time_window)}"
        f".png"
    )

    fig_top.savefig(
        output_dir / top_filename,
        dpi=200,
        bbox_inches="tight",
    )

    plt.close(fig_top)
    
        # ====================================================
    # NEW FIGURE : MEAN + RELATIVE ERROR (95% CI)
    # ====================================================

    fig_bottom, (ax_mean, ax_rel) = plt.subplots(
        2,
        1,
        figsize=(16, 10),
        sharex=True,
        gridspec_kw={
            "height_ratios": [2, 1]
        }
    )

    for study in studies:

        data = stats[study]

        keys = sorted(data.keys())

        if not keys:
            continue

        # ------------------------------------------------
        # X AXIS
        # ------------------------------------------------

        if group_by[0] == "pos":

            keys = sorted(
                keys,
                key=lambda k: pos_to_order(k[0])
            )

            x_vals = np.arange(len(keys))

            labels = []

            for k in keys:

                if k[0] == "HC":

                    labels.append(
                        r"$x_{HC}$"
                        "\n(135.934 m)"
                    )

                else:

                    labels.append(
                        pos_to_label(k[0])
                    )

        elif group_by[0] == "depth":

            shift = space_shift.get(
                study,
                0.0,
            )

            x_vals = np.array([
                k[0] + shift
                for k in keys
            ])

            labels = None

        else:

            x_vals = np.array([
                k[0]
                for k in keys
            ])

            labels = None

        mean_vals = np.array([
            data[k]["mean"]
            for k in keys
        ])

        # ------------------------------------------------
        # MEAN
        # ------------------------------------------------

        ax_mean.plot(
            x_vals,
            mean_vals,
            color=study_colors[study],
            marker="o",
            linewidth=2,
        )

        # ------------------------------------------------
        # RELATIVE ERROR + CI
        # ------------------------------------------------

        if study != reference_study:

            common_keys = sorted(
                set(data.keys())
                &
                set(ref_data.keys())
            )

            if not common_keys:
                continue

            if group_by[0] == "pos":

                common_keys = sorted(
                    common_keys,
                    key=lambda k:
                    pos_to_order(k[0])
                )

                x_err = np.arange(
                    len(common_keys)
                )

            elif group_by[0] == "depth":

                shift = space_shift.get(
                    study,
                    0.0,
                )

                x_err = np.array([
                    k[0] + shift
                    for k in common_keys
                ])

            else:

                x_err = np.array([
                    k[0]
                    for k in common_keys
                ])

            errors = []
            err_low = []
            err_high = []

            tasks = [
                (
                    key,
                    ref_data[key]["wave"],
                    data[key]["wave"],
                )
                for key in common_keys
            ]

            with ProcessPoolExecutor() as ex:

                results = list(
                    ex.map(
                        bca_worker,
                        tasks,
                    )
                )

            for key, err, ci_low, ci_high in results:

                errors.append(err)

                err_low.append(
                    err - ci_low
                )

                err_high.append(
                    ci_high - err
                )

            errors = np.asarray(errors)

            lower = errors - np.asarray(err_low)
            upper = errors + np.asarray(err_high)

            ax_rel.plot(
                x_err,
                errors,
                color=study_colors[study],
                linewidth=2,
            )

            ax_rel.fill_between(
                x_err,
                lower,
                upper,
                color=study_colors[study],
                alpha=0.20,
            )

        if labels is not None:

            ax_rel.set_xticks(
                x_vals
            )

            ax_rel.set_xticklabels(
                labels
            )

    # ====================================================
    # FORMATTING
    # ====================================================

    ax_mean.set_ylabel(
        "H [m]"
    )

    ax_mean.grid()

    ax_rel.axhline(
        0,
        color="black",
        linestyle=":"
    )

    ax_rel.grid()

    ax_rel.set_ylabel(
        "Relative Error [%]"
    )

    ax_rel.set_xlabel(
        get_xlabel(group_by[0])
    )

    # ====================================================
    # LEGENDS
    # ====================================================

    mean_handles = [
        Line2D(
            [0],
            [0],
            color=study_colors[s],
            marker="o",
            lw=3,
            label=f"{s}",
        )
        for s in studies
    ]

    error_handles = [
        Line2D(
            [0],
            [0],
            color="black",
            lw=2,
            label="Relative Error",
        ),
        Line2D(
            [0],
            [0],
            color="black",
            lw=8,
            alpha=0.20,
            label="95% CI",
        ),
    ]

    fig_bottom.legend(
        handles=mean_handles,
        bbox_to_anchor=(0.87, 0.88),
        loc="upper left",
        title="Mean",
        frameon=True,
    )

    fig_bottom.legend(
        handles=error_handles,
        bbox_to_anchor=(0.87, 0.62),
        loc="upper left",
        title="Error Metrics",
        frameon=True,
    )

    # ====================================================
    # LAYOUT
    # ====================================================

    fig_bottom.subplots_adjust(
        left=0.08,
        right=0.83,
        top=0.88,
        bottom=0.10,
        hspace=0.12,
    )

    fig_bottom.suptitle(
        f"Mean Wave Height and Relative Error (95% CI) | Reference={reference_study} | {format_filters(filters)}",
        fontsize=16,
        y=0.98,
    )

    # ====================================================
    # SAVE
    # ====================================================

    bottom_filename = (
        f"mean_relative_error_95ci_"
        f"{'-'.join(group_by)}_"
        f"{dt_mode}_"
        f"{format_filters(filters)}_"
        f"{format_time_window(time_window)}"
        f".png"
    )

    fig_bottom.savefig(
        output_dir / bottom_filename,
        dpi=200,
        bbox_inches="tight",
    )

    plt.close(fig_bottom)