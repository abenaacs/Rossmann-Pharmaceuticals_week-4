import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset by handling missing values and outliers.

    Args:
        data (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    try:
        logging.info("Handling missing values.")
        if "CompetitionDistance" in data.columns:
            data["CompetitionDistance"].fillna(
                data["CompetitionDistance"].median(), inplace=True
            )
        else:
            raise KeyError("'CompetitionDistance' column is missing in the dataset")

        data.dropna(subset=["Sales"], inplace=True)  # Drop rows with missing sales

        logging.info("Handling outliers.")
        data = data[data["Sales"] <= 5000]
        print("Cleaned Data: ", data.head())

        return data
    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        raise
