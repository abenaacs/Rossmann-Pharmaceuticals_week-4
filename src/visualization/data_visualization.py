import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def visualize_and_save(data: pd.DataFrame, output_dir: str) -> None:
    """
    Perform exploratory data analysis and save visualizations.

    Args:
        data (pd.DataFrame): Input DataFrame.
        output_dir (str): Directory to save visualizations.

    Returns:
        None
    """
    try:
        # Promo distribution
        logging.info("Visualizing promo distribution.")
        sns.countplot(data=data, x="Promo2", hue="StoreType")
        plt.title("Promo Distribution in Train Data")
        plt.savefig(f"{output_dir}/promo_distribution.png")
        plt.close()

        # Sales during holidays
        logging.info("Visualizing sales during holidays.")
        sns.boxplot(x="StateHoliday", y="Sales", data=data)
        plt.title("Sales During Holidays")
        plt.savefig(f"{output_dir}/sales_during_holidays.png")
        plt.close()

        # Seasonal promo behavior
        logging.info("Visualizing seasonal promo behavior.")
        sns.countplot(x="PromoInterval", data=data)
        plt.title("Seasonal Promo Behavior")
        plt.savefig(f"{output_dir}/seasonal_promo_behavior.png")
        plt.close()

        # Sales vs. number of customers
        logging.info("Visualizing sales vs. number of customers.")
        sns.scatterplot(x="Customers", y="Sales", data=data)
        plt.title("Sales vs. Number of Customers")
        plt.savefig(f"{output_dir}/sales_vs_customers.png")
        plt.close()

        # Impact of promos on sales
        logging.info("Visualizing impact of promos on sales.")
        sns.boxplot(x="Promo2", y="Sales", data=data)
        plt.title("Impact of Promo on Sales")
        plt.savefig(f"{output_dir}/impact_of_promo_on_sales.png")
        plt.close()

        # Sales based on assortment types
        logging.info("Visualizing sales based on assortment types.")
        sns.boxplot(x="Assortment", y="Sales", data=data)
        plt.title("Sales Based on Assortment Type")
        plt.savefig(f"{output_dir}/sales_based_on_assortment.png")
        plt.close()

        # Competition distance vs. sales
        logging.info("Visualizing competition distance vs. sales.")
        sns.scatterplot(x="CompetitionDistance", y="Sales", data=data)
        plt.title("Competition Distance vs. Sales")
        plt.savefig(f"{output_dir}/competition_distance_vs_sales.png")
        plt.close()

    except Exception as e:
        logging.error(f"Error during visualization: {e}")
        raise
