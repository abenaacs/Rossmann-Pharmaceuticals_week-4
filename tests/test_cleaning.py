import unittest
import pandas as pd
from cleaning import clean_data, handle_missing_values


class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        """Set up a sample dataframe for testing."""
        self.sample_data = pd.DataFrame(
            {
                "Sales": [1000, 2000, None, 1500],
                "Promo": [1, 0, 1, None],
                "CompetitionDistance": [300.0, None, 1500.0, 1200.0],
            }
        )

    def test_clean_data(self):
        """Test that clean_data removes rows with NaN in critical columns."""
        cleaned_data = clean_data(self.sample_data, critical_columns=["Sales", "Promo"])
        self.assertEqual(
            len(cleaned_data), 2
        )  # Rows with NaN in 'Sales' or 'Promo' are removed.

    def test_handle_missing_values(self):
        """Test that handle_missing_values fills missing values correctly."""
        filled_data = handle_missing_values(self.sample_data, method="median")
        self.assertFalse(filled_data.isnull().any().any())  # No missing values left.


if __name__ == "__main__":
    unittest.main()
