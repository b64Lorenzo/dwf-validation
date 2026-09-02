"""
Wave Height Signal Processing
=============================

Module
------
waveheight.processing.processor

Description
-----------
Functions responsible for:

* Metadata extraction
* Probe coordinate extraction
* Fourier analysis
* Wavefield preparation

Author
------
Lorenzo Zambelli
"""

from __future__ import annotations

import re

import numpy as np

from pymarin_timedom.fft import direct

from utils.io import read_db

from waveheight.config import (
    FOLDER_RE,
)


# ============================================================
# PROBE COORDINATES
# ============================================================

PROBE_RE = re.compile(
    r"WaveElev_probe_x([mp]\d+)_y([mp]\d+)"
)


def decode_coordinate(value: str):
    """
    Examples
    --------
    m150 -> -150
    p150 -> 150
    """

    sign = -1 if value[0] == "m" else 1

    return sign * int(value[1:])


def extract_coordinates(
    signal_name: str,
):
    """
    Example
    -------
    WaveElev_probe_xm150_yp48

    Returns
    -------
    tuple[int, int] | None
    """

    match = PROBE_RE.search(
        signal_name
    )

    if not match:
        return None

    xPos = decode_coordinate(
        match.group(1)
    )

    yPos = decode_coordinate(
        match.group(2)
    )

    return (
        xPos,
        yPos,
    )


# ============================================================
# FOURIER COEFFICIENT
# ============================================================

def extract_fourier_component(
    signal,
    time,
    omega_target,
):
    """
    Extract complex Fourier coefficient
    at the target angular frequency.

    Parameters
    ----------
    signal : ndarray

    time : ndarray

    omega_target : float
        Angular frequency [rad/s]

    Returns
    -------
    complex
    """

    signal = np.asarray(
        signal,
        dtype=float,
    )

    signal = (
        signal
        - np.mean(signal)
    )

    dt = np.mean(
        np.diff(time)
    )

    omega_fft, fft = direct(
        signal,
        dt=dt,
    )

    index = np.argmin(
        np.abs(
            omega_fft
            - omega_target
        )
    )

    return fft[index]


# ============================================================
# PROCESS FILE
# ============================================================

def process_file(
    csv_path,
    logger=None,
):
    """
    Process simulation file.

    Returns
    -------
    list

    [
        {
            angle
            dx
            dt
            freq
            pan
            xPos
            yPos
            real
            imag
            abs
            phase
        }
    ]
    """

    try:

        folder = csv_path.parent.name

        match = FOLDER_RE.search(
            folder
        )

        if not match:

            if logger:
                logger.warning(
                    "Failed folder parsing: %s",
                    folder,
                )

            return []

        meta = {
            key: float(value)
            for key, value
            in match.groupdict().items()
        }

        meta["angle"] = int(
            meta["angle"]
        )

        meta["pan"] = int(
            meta["pan"]
        )

        db = read_db(
            csv_path
        )

        if db is None:

            if logger:
                logger.warning(
                    "Database is None: %s",
                    csv_path,
                )

            return []

        if logger:
            logger.info(
                "Loaded database with %d signals",
                len(db.keys),
            )

        # =====================================================
        # TIME SIGNAL
        # =====================================================

        time_key = None

        for key in db.keys:

            if key.name.lower() == "time":

                time_key = key

                break

        if time_key is None:

            if logger:
                logger.warning(
                    "No time signal found."
                )

            return []

        time = np.asarray(
            db[time_key].data
        ).reshape(-1)

        if time.size < 10:

            if logger:
                logger.warning(
                    "Time signal too short."
                )

            return []

        omega = meta["freq"]

        results = []

        n_wave_signals = 0

        # =====================================================
        # PROBE LOOP
        # =====================================================

        for key in db.keys:

            signal_name = key.name

            if (
                "WaveElev_probe"
                not in signal_name
            ):
                continue

            n_wave_signals += 1

            coordinates = (
                extract_coordinates(
                    signal_name
                )
            )

            if coordinates is None:
                continue

            try:

                signal_obj = db[key]

            except Exception:
                continue

            if signal_obj is None:
                continue

            if signal_obj.data is None:
                continue

            signal = np.asarray(
                signal_obj.data
            ).reshape(-1)

            if signal.size != time.size:
                continue

            if signal.size < 10:
                continue

            coefficient = (
                extract_fourier_component(
                    signal=signal,
                    time=time,
                    omega_target=omega,
                )
            )

            xPos, yPos = coordinates

            result = meta.copy()

            result["xPos"] = xPos
            result["yPos"] = yPos

            result["real"] = float(
                np.real(
                    coefficient
                )
            )

            result["imag"] = float(
                np.imag(
                    coefficient
                )
            )

            result["abs"] = float(
                np.abs(
                    coefficient
                )
            )

            result["phase"] = float(
                np.angle(
                    coefficient
                )
            )

            results.append(
                result
            )

        if logger:

            logger.info(
                "Wave signals found: %d",
                n_wave_signals,
            )

            logger.info(
                "Records returned: %d",
                len(results),
            )

        return results

    except Exception as exc:

        if logger:

            logger.exception(
                "Failed processing %s. Error: %s",
                csv_path,
                exc,
            )

        return []