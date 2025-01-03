import pandas as pd


def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise FileNotFoundError(f"Error loading file {file_path}: {e}")
