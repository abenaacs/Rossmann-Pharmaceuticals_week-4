import unittest
import pandas as pd
from src.data_preprocessing.data_cleaning import clean_data


class TestDataCleaning(unittest.TestCase):
    def test_clean_data(self):
        # Mock merged data for testing
        merged_data = pd.DataFrame(
            {
                "Store": [1, 2],
                "DayOfWeek": [5, 5],
                "Date": ["2015-07-31", "2015-07-30"],
                "Sales": [5263, 6064],
                "Customers": [555, 625],
                "Open": [1, 1],
                "Promo": [1, 1],
                "StateHoliday": ["0", "0"],
                "SchoolHoliday": [1, 0],
            }
        )

        # Call clean_data and check results
        cleaned_data = clean_data(merged_data)
        self.assertIsNotNone(cleaned_data)
        self.assertIsInstance(cleaned_data, pd.DataFrame)

        # Ensure unnecessary columns are dropped or transformed as expected
        self.assertIn("Sales", cleaned_data.columns)
        self.assertNotIn("Date", cleaned_data.columns)  # Example transformation
