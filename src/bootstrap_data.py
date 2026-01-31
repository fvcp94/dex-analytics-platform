from src.data_gen import generate_dex_data
from src.io import save_tables
import os

def bootstrap():
    if not os.listdir("data/processed"):
        save_tables(generate_dex_data())
