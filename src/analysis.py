import logging
from data_preprocessing.data_cleaning import clean_data
from src.data_preprocessing.data_merging import merge_data
from src.visualization.visualization import save_visualization, plot_promo_sales
from utils.utils import load_csv

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


def main():
    # Step 1: Load and merge data
    logging.info("Starting the data pipeline.")
    full_data = merge_data("train.txt", "test.txt", "store.txt")

    # Step 2: Clean data
    cleaned_data = clean_data(full_data)

    # Step 3: Visualize and save results
    save_visualization(
        lambda: plot_promo_sales(cleaned_data), "promo_sales_comparison.png"
    )


if __name__ == "__main__":
    main()
