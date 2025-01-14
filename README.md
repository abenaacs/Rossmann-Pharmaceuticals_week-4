# Rossmann Pharmaceuticals Sales Prediction

This project focuses on analyzing and predicting sales for Rossmann Pharmaceuticals using historical data. It leverages data preprocessing, exploratory analysis, and machine learning to generate insights and predictive models. The dataset includes features such as sales, customers, promotions, and store-specific information.

## Project Overview

The primary goals of this project are:

1. **Data Cleaning and Preprocessing**: Handle missing values, incorrect data types, and merge datasets for seamless analysis.
2. **Exploratory Data Analysis (EDA)**: Gain insights into the data distribution, trends, and patterns that influence sales.
3. **Modeling and Prediction**: Develop robust machine learning models to forecast sales and assess model performance.

## Project Structure

The repository is organized into the following directories and files:

- **`data/`**: Contains raw and processed datasets:
  - `train.csv`: Historical training data.
  - `test.csv`: Test dataset for predictions.
  - `store.csv`: Store-specific information.
- **`src/`**: Source code for various project tasks:
  - `data_preprocessing/`: Scripts for data loading, cleaning, and feature engineering.
  - `models/`: Machine learning model scripts.
  - `utilities/`: Utility functions for repetitive tasks.
- **`notebooks/`**: Jupyter notebooks for EDA and detailed analysis.
- **`tests/`**: Unit tests to ensure reliability of key functions.
- **`README.md`**: This overview file with project instructions and details.
- **`requirements.txt`**: Lists required Python packages.
- **`models/`**: Pretrained model files saved in `.h5` format.

## Requirements

- Python 3.7 or higher
- Key libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, tensorflow, keras

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/abenaacs/Rossmann-Pharmaceuticals_week-4.git
cd Rossmann-Pharmaceuticals_week-4
```

### Loading and Cleaning Data

Run the following to load and clean your data:

```python
from src.data_preprocessing.data_loader import load_data
from src.data_preprocessing.data_cleaning import clean_data

# File paths
train_data_path = 'data/train.csv'
test_data_path = 'data/test.csv'
store_data_path = 'data/store.csv'

# Load and clean data
merged_data = load_data(train_data_path, test_data_path, store_data_path)
cleaned_data = clean_data(merged_data)
```

### Exploratory Data Analysis

For EDA, open and run the provided Jupyter notebook:

```bash
jupyter notebook notebooks/EDA_notebook.ipynb
```

### Training and Predicting

Train your model and generate predictions using the following:

```python
from src.models.model_training import train_model
from src.models.prediction import predict_sales

model, history = train_model(cleaned_data)
predictions = predict_sales(model, cleaned_data)
```

## Running Unit Tests

Ensure the reliability of the codebase with unit tests:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Let me know if any additional refinements are needed!
