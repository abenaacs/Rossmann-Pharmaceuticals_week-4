import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def merge_data(train_file: str, test_file: str, store_file: str) -> pd.DataFrame:
    """
    Load and merge the train, test, and store data into a single dataframe.

    Args:
        train_file (str): Path to the train data CSV file.
        test_file (str): Path to the test data CSV file.
        store_file (str): Path to the store data CSV file.

    Returns:
        pd.DataFrame: Merged dataset.
    """
    try:
        # Load the datasets
        train_data = pd.read_csv(train_file)
        test_data = pd.read_csv(test_file)
        store_data = pd.read_csv(store_file)

        # Merge the train and test datasets with the store data
        logging.info("Merging train and store data.")
        train_data = pd.merge(train_data, store_data, on="Store", how="left")
        test_data = pd.merge(test_data, store_data, on="Store", how="left")

        # Combine the datasets for analysis
        full_data = pd.concat([train_data, test_data], ignore_index=True)
        logging.info(
            f"Merged dataset has {full_data.shape[0]} rows and {full_data.shape[1]} columns."
        )

        return full_data
    except Exception as e:
        logging.error(f"Error loading and merging datasets: {e}")
        raise
