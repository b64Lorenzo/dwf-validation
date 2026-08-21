# ==========================================
# downsample_timedb_folder.py
# ==========================================

from pathlib import Path
import numpy as np
from tqdm import tqdm

from pymarin.io import read_timedb
from pymarin.io.csv import write_table
from pymarin import Signal, SignalSet


# ==========================================
# CONFIG
# ==========================================

ROOT_DIR = Path(r"F:\validation\data\fixed\angle135")   # ✅ root folder
STEP = 25                                               # ✅ downsampling factor
OVERWRITE = True                                       # False → create new files


# ==========================================
# READ
# ==========================================

def read_db(path):
    try:
        db = read_timedb(str(path))
        return db if db.keys else None
    except Exception as e:
        print(f"Failed: {path} -> {e}")
        return None


# ==========================================
# DOWNSAMPLE
# ==========================================

def downsample_db(db, step):

    signals_out = []

    # ✅ time = FIRST signal
    first_key = db.keys[0]
    time_sig_obj = db[first_key]

    if time_sig_obj is None or time_sig_obj.data is None:
        return SignalSet([])

    time = np.asarray(time_sig_obj.data).reshape(-1)

    if len(time) < step:
        step = 1

    time_ds = time[::step]

    # ✅ create time signal
    time_signal = Signal(first_key.name, time_ds)
    signals_out.append(time_signal)

    # ✅ other signals
    for key in db.keys[1:]:

        sig = db[key]

        if sig is None or sig.data is None:
            continue

        data = np.asarray(sig.data).reshape(-1)

        data_ds = data[::step]

        # ✅ safety: match length
        n = min(len(time_ds), len(data_ds))
        data_ds = data_ds[:n]

        signals_out.append(
            Signal(
                sig.name,
                data_ds,
                leads=[time_signal]
            )
        )

    return SignalSet(signals_out)


# ==========================================
# PROCESS SINGLE FILE
# ==========================================

def process_file(csv_path):

    db = read_db(csv_path)
    if db is None:
        return False

    ds = downsample_db(db, STEP)

    # ✅ output naming
    if OVERWRITE:
        out_path = csv_path
    else:
        out_path = csv_path.with_name(csv_path.stem + "_ds.csv")

    write_table(str(out_path), ds, overwrite=True)

    return True


# ==========================================
# MAIN
# ==========================================

from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
import os


def main():

    csv_files = list(ROOT_DIR.rglob("*.csv"))

    if not csv_files:
        print("No CSV files found.")
        return

    print(f"✅ Found {len(csv_files)} files")

    success = 0
    failed = 0

    # ✅ choose number of workers
    N_WORKERS = min(8, os.cpu_count() or 1)

    with ProcessPoolExecutor(max_workers=N_WORKERS) as ex:

        futures = [ex.submit(process_file, f) for f in csv_files]

        for f in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="Downsampling",
            unit="file",
            dynamic_ncols=True,
        ):
            try:
                result = f.result()
                if result:
                    success += 1
                else:
                    failed += 1
            except:
                failed += 1

    print(f"\n✅ Done: {success}/{len(csv_files)} successful")
    print(f"⚠️ Failed/skipped: {failed}")


# ==========================================
# ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()