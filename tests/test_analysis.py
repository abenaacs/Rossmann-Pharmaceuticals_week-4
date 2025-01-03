import unittest
from src.analysis import load_data, analyze_data


class TestAnalysisPipeline(unittest.TestCase):
    def test_load_data(self):
        """Test that load_data correctly loads a CSV file into a DataFrame."""
        sample_path = "data/sample_data.csv"
        with open(sample_path, "w") as f:
            f.write("Sales,Promo\n1000,1\n2000,0")

        df = load_data(sample_path)
        self.assertEqual(df.shape, (2, 2))  # Ensure the correct shape is loaded.

    def test_analyze_data(self):
        """Test the analyze_data pipeline with a small sample dataset."""
        sample_data = {"Sales": [1000, 2000, 3000], "Promo": [1, 0, 1]}
        try:
            analyze_data(sample_data)  # Just test if it runs without exceptions.
        except Exception as e:
            self.fail(f"analyze_data raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
