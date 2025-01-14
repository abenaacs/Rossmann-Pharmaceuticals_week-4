#### Overview:

This section describes the key functions and scripts used in the project.

1. **Preprocessing Functions:**

   - `convert_datetime(data)`: Converts the `Date` column into datetime format and extracts year, month, day, and week features.
   - `encode_categorical(data)`: Encodes categorical variables using one-hot encoding.

2. **Modeling Scripts:**

   - `build_lstm_model(input_shape)`: Constructs an LSTM model architecture.
   - `train_model(model, X_train, y_train)`: Trains the LSTM model using the provided data.
   - `evaluate_model(model, X_test, y_test)`: Evaluates model performance on the test dataset.

3. **Utility Functions:**
   - `visualize_sales_distribution(data)`: Plots sales distribution.
   - `plot_actual_vs_predicted(y_actual, y_pred)`: Compares actual vs. predicted sales with a line plot.

#### Scripts Structure:

- `app.py`: Main script for running the prediction pipeline.
- `notebook_code.py`: Contains notebook-converted Python code for standalone execution.
- `utils.py`: Includes reusable functions for preprocessing and visualization.

#### Key Directories:

- `data/`: Contains the dataset.
- `models/`: Stores the trained model.

---
