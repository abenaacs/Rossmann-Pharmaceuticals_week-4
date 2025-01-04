import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def load_data(train_path: str, test_path: str, store_path: str) -> pd.DataFrame:
    """
    Load and merge datasets for analysis.

    Args:
        train_path (str): Path to the training dataset.
        test_path (str): Path to the testing dataset.
        store_path (str): Path to the store dataset.

    Returns:
        pd.DataFrame: Merged DataFrame.
    """
    try:
        logging.info("Loading datasets.")
        train_data = pd.read_csv(train_path)
        test_data = pd.read_csv(test_path)
        store_data = pd.read_csv(store_path)

        logging.info("Merging datasets.")
        data = pd.merge(train_data, store_data, on="Store", how="left")
        print("Sample Merged Data: ", data.head())
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise
