import pandas as pd
import logging
import os
import matplotlib.pyplot as plt

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        logging.info(f"Loading CSV file: {file_path}")
        data = pd.read_csv(file_path)
        logging.info(f"Loaded {len(data)} rows and {len(data.columns)} columns.")
        return data
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
        raise


def merge_datasets(train_file: str, test_file: str, store_file: str) -> pd.DataFrame:
    """
    Merges the training and test datasets with the store data.

    Args:
        train_file (str): Path to the training data CSV.
        test_file (str): Path to the test data CSV.
        store_file (str): Path to the store data CSV.

    Returns:
        pd.DataFrame: Merged dataset.
    """
    try:
        train_data = load_csv(train_file)
        test_data = load_csv(test_file)
        store_data = load_csv(store_file)

        # Merge datasets
        logging.info("Merging train and store data.")
        train_data = pd.merge(train_data, store_data, on="Store", how="left")
        test_data = pd.merge(test_data, store_data, on="Store", how="left")

        # Concatenate train and test datasets
        full_data = pd.concat([train_data, test_data], ignore_index=True)
        logging.info(
            f"Full merged dataset has {full_data.shape[0]} rows and {full_data.shape[1]} columns."
        )

        return full_data
    except Exception as e:
        logging.error(f"Error merging datasets: {e}")
        raise


def save_visualization(plt, plot_name: str, directory: str = "visualizations"):
    """
    Saves a plot as an image file.

    Args:
        plt (matplotlib.pyplot): The plot to save.
        plot_name (str): The name for the saved plot file.
        directory (str): Directory where the plot should be saved (default is 'visualizations').
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

        plot_path = os.path.join(directory, plot_name)
        plt.savefig(plot_path)
        logging.info(f"Saved visualization: {plot_path}")
    except Exception as e:
        logging.error(f"Error saving visualization: {e}")
        raise
