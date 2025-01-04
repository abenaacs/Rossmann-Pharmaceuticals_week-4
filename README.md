# Rossmann Pharmaceuticals Project

This project involves analyzing and predicting sales for Rossmann pharmaceutical stores using historical data. The data includes various features like sales, customers, promotions, and store information. We clean, process, and analyze the data to generate insights and predictive models.

## Project Structure

The project is organized into the following directories and files:

- `data/`: Contains raw and processed data files.
- `src/`: Contains source code for data loading, preprocessing, analysis, and model training.
- `tests/`: Contains unit tests for data cleaning and other functions.
- `notebooks/`: Contains Jupyter notebooks for exploratory data analysis (EDA).
- `README.md`: Project overview and instructions.

## Requirements

- Python 3.7+
- Required libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, etc.

## Installation

1. Clone the repository:
   python

   ```bash
   git clone https://github.com/abenaacs/Rossmann-Pharmaceuticals_week-4.git
   ```

2. Navigate to the project directory:
   python

   ```bash
   cd rossmann-pharmaceuticals
   ```

3. Install the required dependencies:
   python
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

### Loading Data

To load the data and merge datasets, run the following command in Python:

python

```bash
from src.data_preprocessing.data_loader import load_data

train_data_path = 'data/train.csv'
test_data_path = 'data/test.csv'
store_data_path = 'data/store.csv'

merged_data = load_data(train_data_path, test_data_path, store_data_path)
```

## Cleaning Data

Once data is loaded, you can clean it with:

python

```bash
from src.data_preprocessing.data_cleaning import clean_data

cleaned_data = clean_data(merged_data)

```

## Running Unit Tests

To run the unit tests for the project, use the following command:
python

```bash
python -m unittest discover -s tests
```

## Contributing

We welcome contributions! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
