from pathlib import Path
import pandas as pd

BASE = Path("data/processed")
BASE.mkdir(parents=True, exist_ok=True)

def save_tables(tables):
    for k,v in tables.items():
        v.to_parquet(BASE / f"{k}.parquet", index=False)

def load_table(name):
    return pd.read_parquet(BASE / f"{name}.parquet")
