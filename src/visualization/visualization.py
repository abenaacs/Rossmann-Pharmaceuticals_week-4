import seaborn as sns
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def save_visualization(plot_func, plot_filename: str):
    """
    Generates a plot and saves it to the specified filename.

    Args:
        plot_func (function): The function that generates the plot.
        plot_filename (str): The filename to save the plot.

    Returns:
        None
    """
    try:
        logging.info(f"Saving visualization: {plot_filename}")
        plot_func()
        plt.savefig(plot_filename)
        logging.info(f"Saved plot: {plot_filename}")
    except Exception as e:
        logging.error(f"Error saving plot {plot_filename}: {e}")
        raise


# Example of a plot function
def plot_promo_sales(data):
    """
    Plots the impact of promo on sales.

    Args:
        data (pd.DataFrame): The dataset to plot.

    Returns:
        None
    """
    sns.boxplot(x="Promo2", y="Sales", data=data)
    plt.title("Impact of Promo on Sales")
    plt.show()
