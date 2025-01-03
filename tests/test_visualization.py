import unittest
import matplotlib.pyplot as plt
from eda_plots import plot_sales_trend


class TestVisualization(unittest.TestCase):
    def plot_sales_during_holidays(self):
        """Test if plot_sales_trend runs without errors and produces a figure."""
        try:
            fig = plot_sales_trend([1000, 2000, 3000], [1, 2, 3])
            self.assertIsInstance(
                fig, plt.Figure
            )  # Ensure a matplotlib figure is returned.
        except Exception as e:
            self.fail(f"plot_sales_trend raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
