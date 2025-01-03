import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the data by handling missing values and removing outliers.

    Args:
        data (pd.DataFrame): The raw data to clean.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    try:
        logging.info("Cleaning data: handling missing values and outliers.")

        # Fill missing 'CompetitionDistance' with median value
        data["CompetitionDistance"].fillna(
            data["CompetitionDistance"].median(), inplace=True
        )

        # Drop rows with missing 'Sales' values
        data.dropna(subset=["Sales"], inplace=True)

        # Removing outliers (e.g., sales > 5000)
        data = data[data["Sales"] <= 5000]

        logging.info("Data cleaned successfully.")
        return data
    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        raise
