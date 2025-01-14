import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging

logging.basicConfig(level=logging.INFO)


class DataPreprocessor:
    def __init__(self, scaler=None):
        self.scaler = scaler or StandardScaler

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess the dataset.

        Args:
        df (pd.DataFrame): Input DataFrame.

        Returns:
        pd.DataFrame: Preprocessed DataFrame.
        """
        try:
            logging.info("Starting preprocessing...")

            # Validate required columns
            required_columns = ["Date"]
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise KeyError(f"Missing required columns: {missing_columns}")

            # Convert dates and extract features
            df["Date"] = pd.to_datetime(df["Date"])
            df["Weekday"] = df["Date"].dt.weekday
            df["Is_Weekend"] = df["Weekday"].isin([5, 6]).astype(int)
            df["Month"] = df["Date"].dt.month
            df["Day"] = df["Date"].dt.day
            df["Year"] = df["Date"].dt.year

            # # Scale numeric columns
            # numeric_cols = ["Sales", "Customers"]
            # df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])

            logging.info("Preprocessing completed.")
            return df
        except Exception as e:
            logging.error(f"Error in preprocessing: {e}")
            raise
