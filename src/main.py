from data_preprocessing.data_loader import load_data
from data_preprocessing.data_cleaning import clean_data
from visualization.data_visualization import visualize_and_save
from modeling.sales_prediction import build_and_serialize_models
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    try:
        # Define file paths
        current_dir = os.getcwd()
        train_path = os.path.join(current_dir, "./data/train.csv")
        test_path = os.path.join(current_dir, "./data/test.csv")
        store_path = os.path.join(current_dir, "./data/store.csv")
        output_dir = os.path.join(current_dir, "./visualizations")
        model_dir = os.path.join(current_dir, "./models")

        # Ensure necessary directories exist
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(model_dir, exist_ok=True)

        # Step 1: Load Data
        logging.info("Loading data...")
        data = load_data(train_path, test_path, store_path)

        # Step 2: Clean Data
        logging.info("Cleaning data...")
        data = clean_data(data)

        # Step 3: Perform EDA and save visualizations
        logging.info("Performing EDA and saving visualizations...")
        visualize_and_save(data, output_dir)

        # Step 4: Build and Serialize Models
        logging.info("Building and serializing models...")
        build_and_serialize_models(data, model_dir)

        logging.info("Pipeline execution completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred in the main pipeline: {e}")
        raise


if __name__ == "__main__":
    main()
