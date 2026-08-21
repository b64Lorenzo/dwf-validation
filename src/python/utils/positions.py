# utils/positions.py

"""
Position Utilities
==================

Utilities for handling hydrodynamic-center-relative
probe positions.
"""

from __future__ import annotations


def normalize(position):
    """
    Convert long-form position names into a
    standardized representation.
    """

    mapping = {
        "-2xhalfHydCenter": "-2xHC",
        "-halfHydCenter": "-1xHC",
        "halfHydCenter": "+1xHC",
        "2xhalfHydCenter": "+2xHC",
        "HC": "0xHC",
        "-2xHC": "-2xHC",
        "-1xHC": "-1xHC",
        "0xHC": "0xHC",
        "+1xHC": "+1xHC",
        "+2xHC": "+2xHC",
    }

    return mapping.get(position, position)


def pos_to_order(position):
    """
    Convert a position identifier into a sortable value.
    """

    position = normalize(position)

    order = {
        "-2xHC": -2,
        "-1xHC": -1,
        "0xHC": 0,
        "HC": 0,
        "+1xHC": 1,
        "+2xHC": 2,
    }

    return order.get(position, 0)


def pos_to_label(position):
    """
    Convert a position identifier into a LaTeX label.
    """

    labels = {
        "-2xHC": r"$-2x_{HC}$",
        "-1xHC": r"$-\frac{1}{2}x_{HC}$",
        "HC": r"$x_{HC}$",
        "0xHC": r"$x_{HC}$",
        "+1xHC": r"$\frac{1}{2}x_{HC}$",
        "+2xHC": r"$2x_{HC}$",
    }

    return labels.get(position, str(position))
    
    
def get_xlabel(key):
    """
    Return human-readable axis labels.
    """

    labels = {
        "freq": r"Angular frequency $\omega$ [rad/s]",
        "depth": r"$Y$ [m]",
        "angle": "Angle [deg]",
        "pos": "Position X [m] w.r.t Hydrodynamic center",
        "dt": "Points per period",
        "dx": "dx [m]",
        "pan": "Panel ID",
    }

    return labels.get(key, key)