from data_preprocessing.data_loader import load_data
from data_preprocessing.data_cleaning import clean_data
from visualization.data_visualization import visualize_and_save
import os


def main():
    # Define file paths
    current_dir = os.getcwd()
    train_path = os.path.join(current_dir, "./data/train.csv")
    test_path = os.path.join(current_dir, "./data/test.csv")

    store_path = os.path.join(current_dir, "./data/store.csv")
    output_dir = os.path.join(current_dir, "./visualizations")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load data and Merge Data
    data = load_data(train_path, test_path, store_path)

    # Clean data and Outliers
    data = clean_data(data)

    # Perform EDA and save visualizations
    visualize_and_save(data, output_dir)


if __name__ == "__main__":
    main()
