from pathlib import Path
import pandas as pd

# Always resolve paths relative to repo root (works locally + Streamlit Cloud)
REPO_ROOT = Path(__file__).resolve().parents[1]
BASE = REPO_ROOT / "data" / "processed"
BASE.mkdir(parents=True, exist_ok=True)

def save_tables(tables: dict):
    for name, df in tables.items():
        df.to_parquet(BASE / f"{name}.parquet", index=False)

def load_table(name: str) -> pd.DataFrame:
    path = BASE / f"{name}.parquet"
    return pd.read_parquet(path)
