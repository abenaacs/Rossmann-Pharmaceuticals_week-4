import unittest
import pandas as pd
import os
from unittest.mock import patch, MagicMock
from src.visualization.data_visualization import visualize_and_save


class TestEDAAnalysis(unittest.TestCase):
    def setUp(self):
        # Sample test data
        self.data = pd.DataFrame(
            {
                "Promo2": [0, 1, 1, 0],
                "StoreType": ["a", "b", "a", "b"],
                "StateHoliday": ["0", "a", "0", "b"],
                "Sales": [1000, 2000, 1500, 3000],
                "PromoInterval": [
                    "Jan,Apr,Jul,Oct",
                    "Feb,May,Aug,Nov",
                    None,
                    "Mar,Jun,Sep,Dec",
                ],
                "Customers": [200, 300, 150, 400],
                "Assortment": ["a", "c", "b", "a"],
                "CompetitionDistance": [500, 1000, 150, 2000],
            }
        )
        self.output_dir = "test_outputs"

        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        # Clean up generated files
        for file in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, file))
        os.rmdir(self.output_dir)

    @patch("src.utils.eda_analysis.plt.savefig")
    def test_visualize_and_save(self, mock_savefig):
        """
        Test the visualize_and_save function for correct execution and file-saving behavior.
        """
        # Mock savefig to prevent actual file creation
        mock_savefig.return_value = None

        # Run the function
        visualize_and_save(self.data, self.output_dir)

        # Check if plt.savefig was called the expected number of times
        self.assertEqual(mock_savefig.call_count, 7)  # 7 visualizations in total

        # Verify specific calls to plt.savefig
        expected_files = [
            "promo_distribution.png",
            "sales_during_holidays.png",
            "seasonal_promo_behavior.png",
            "sales_vs_customers.png",
            "impact_of_promo_on_sales.png",
            "sales_based_on_assortment.png",
            "competition_distance_vs_sales.png",
        ]
        actual_calls = [call.args[0] for call in mock_savefig.call_args_list]
        for expected_file in expected_files:
            self.assertIn(f"{self.output_dir}/{expected_file}", actual_calls)


if __name__ == "__main__":
    unittest.main()
