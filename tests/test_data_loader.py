import unittest
import pandas as pd
import os
from src.data_preprocessing.data_loader import load_data


class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        # Mock paths for testing
        current_dir = os.getcwd()
        train_path = os.path.join(current_dir, "./data/train.csv")
        test_path = os.path.join(current_dir, "./data/test.csv")
        store_path = os.path.join(current_dir, "./data/store.csv")

        # Call load_data and ensure it returns a DataFrame
        merged_data = load_data(train_path, test_path, store_path)
        self.assertIsNotNone(merged_data)
        self.assertIsInstance(merged_data, pd.DataFrame)

        # Check if the merged data has expected columns
        expected_columns = [
            "Store",
            "DayOfWeek",
            "Date",
            "Sales",
            "Customers",
            "Open",
            "Promo",
            "StateHoliday",
            "SchoolHoliday",
            "CompetitionDistance",
        ]
        for col in expected_columns:
            self.assertIn(col, merged_data.columns)
