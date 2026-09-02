"""
Wave Field 2D Plotting
======================

Module
------
waveheight.plotting.plot2d

Author
------
Lorenzo Zambelli
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from waveheight.config import (
    COLORMAPS,
    XLABELS,
)


def build_title(
    data,
):
    """
    Build plot title from metadata.
    """

    first = data[0]

    depth = 30.0

    omega = first["freq"]

    angle = first["angle"]

    return (
        f"Results for depth: {depth:.0f} m | "
        f"ω = {omega:.3f} rad/s | "
        f"angle = {angle:.0f}°"
    )


def build_grid(
    data,
    component,
):

    xs = sorted(
        {
            item["xPos"]
            for item in data
        }
    )

    ys = sorted(
        {
            item["yPos"]
            for item in data
        }
    )

    x_index = {
        value: i
        for i, value in enumerate(xs)
    }

    y_index = {
        value: i
        for i, value in enumerate(ys)
    }

    Z = np.full(
        (
            len(ys),
            len(xs),
        ),
        np.nan,
    )

    for item in data:

        Z[
            y_index[item["yPos"]],
            x_index[item["xPos"]],
        ] = item[component]

    return (
        np.asarray(xs),
        np.asarray(ys),
        Z,
    )


def create_contour(
    ax,
    X,
    Y,
    Z,
    component,
):

    cmap = COLORMAPS.get(
        component,
        "viridis",
    )

    #
    # Real and imaginary
    # symmetric around zero
    #
    if component in (
        "real",
        "imag",
    ):

        vmax = np.nanmax(
            np.abs(Z)
        )

        contour = ax.contourf(
            X,
            Y,
            Z,
            levels=np.linspace(
                -vmax,
                vmax,
                101,
            ),
            cmap=cmap,
        )

    #
    # Amplitude and phase
    #
    else:

        contour = ax.contourf(
            X,
            Y,
            Z,
            levels=100,
            cmap=cmap,
        )

    return contour


def save_component(
    data,
    component,
    output_file,
):

    xs, ys, Z = build_grid(
        data,
        component,
    )

    X, Y = np.meshgrid(
        xs,
        ys,
    )

    fig, ax = plt.subplots(
        figsize=(12, 4),
    )

    fig.suptitle(
        build_title(data),
        fontsize=14,
        fontweight="bold",
    )

    contour = create_contour(
        ax=ax,
        X=X,
        Y=Y,
        Z=Z,
        component=component,
    )

    cbar = fig.colorbar(
        contour,
        ax=ax,
        shrink=0.85,
        pad=0.02,
    )

    cbar.set_label(
        XLABELS.get(
            component,
            component,
        )
    )

    ax.set_title(
        component.upper(),
    )

    ax.set_xlabel(
        XLABELS["xPos"],
    )

    ax.set_ylabel(
        XLABELS["yPos"],
    )

    ax.set_aspect(
        "auto",
    )

    fig.tight_layout(
        rect=[0, 0, 1, 0.93],
    )

    fig.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)


def save_multiplot(
    data,
    components,
    output_file,
):
    """
    Combined figure.

    REAL | IMAG
    ABS  | PHASE
    """

    n = len(
        components
    )

    ncols = 2

    nrows = int(
        np.ceil(
            n / ncols
        )
    )

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(14, 4 * nrows),
        constrained_layout=True,
    )

    fig.suptitle(
        build_title(data),
        fontsize=16,
        fontweight="bold",
    )

    axes = np.atleast_1d(
        axes
    ).ravel()

    for ax, component in zip(
        axes,
        components,
    ):

        xs, ys, Z = build_grid(
            data,
            component,
        )

        X, Y = np.meshgrid(
            xs,
            ys,
        )

        contour = create_contour(
            ax=ax,
            X=X,
            Y=Y,
            Z=Z,
            component=component,
        )

        cbar = fig.colorbar(
            contour,
            ax=ax,
            shrink=0.70,
            pad=0.02,
        )

        cbar.set_label(
            XLABELS.get(
                component,
                component,
            )
        )

        ax.set_title(
            component.upper(),
        )

        ax.set_xlabel(
            XLABELS["xPos"],
        )

        ax.set_ylabel(
            XLABELS["yPos"],
        )

        ax.set_aspect(
            "auto",
        )

    #
    # Hide unused axes
    #
    for ax in axes[len(components):]:
        ax.set_visible(False)

    fig.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)


def plot_2d(
    data,
    output_dir,
    logger,
    plots,
):
    """
    Generate wavefield maps.
    """

    output_dir = Path(
        output_dir,
    )

    logger.info(
        "Creating wavefield maps..."
    )

    # =====================================================
    # INDIVIDUAL FIGURES
    # =====================================================

    for component in plots:

        logger.info(
            "Plotting %s",
            component,
        )

        output_file = (
            output_dir
            / f"{component}.png"
        )

        save_component(
            data=data,
            component=component,
            output_file=output_file,
        )

    # =====================================================
    # COMBINED FIGURE
    # =====================================================

    if len(plots) > 1:

        logger.info(
            "Creating combined figure."
        )

        save_multiplot(
            data=data,
            components=plots,
            output_file=(
                output_dir
                / "wavefield_all.png"
            ),
        )

    logger.info(
        "Finished generating maps."
    )