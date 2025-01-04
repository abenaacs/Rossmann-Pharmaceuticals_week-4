import logging
import os

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


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
