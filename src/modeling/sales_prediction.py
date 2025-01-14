import os
import joblib
from datetime import datetime
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import save_model
import logging
import numpy as np


def preprocess_data(data):
    """
    Preprocess the data for training.
    - Extracts additional features from datetime columns.
    - Handles missing values and scales data.
    """
    # Extract datetime features
    data["Date"] = pd.to_datetime(data["Date"])
    data["Weekday"] = data["Date"].dt.weekday
    data["IsWeekend"] = data["Weekday"] >= 5
    data["Month"] = data["Date"].dt.month
    data["Day"] = data["Date"].dt.day
    data["Year"] = data["Date"].dt.year

    # Scale numeric data
    numeric_features = ["Sales", "Customers"]
    scaler = StandardScaler()
    data[numeric_features] = scaler.fit_transform(data[numeric_features])
    return data


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def build_and_serialize_models(data, model_dir):
    try:
        logging.info("Starting preprocessing...")
        data = preprocess_data(data)

        logging.info("Splitting data for training...")
        X = data[["Store", "Day", "Month", "Year", "Weekday", "IsWeekend"]]
        y = data["Sales"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        logging.info("Training RandomForest model...")
        rf_pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
            ]
        )
        rf_pipeline.fit(X_train, y_train)

        rf_model_path = os.path.join(
            model_dir, f"rf_model_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pkl"
        )
        joblib.dump(rf_pipeline, rf_model_path)
        logging.info(f"RandomForest model saved at {rf_model_path}")

        logging.info("Preparing data for LSTM...")
        time_steps = 30
        lstm_data = data[["Sales"]].values
        X_lstm, y_lstm = [], []
        for i in range(len(lstm_data) - time_steps):
            X_lstm.append(lstm_data[i : i + time_steps])
            y_lstm.append(lstm_data[i + time_steps])
        X_lstm, y_lstm = np.array(X_lstm), np.array(y_lstm)

        logging.info("Training LSTM model...")
        lstm_model = Sequential(
            [
                LSTM(
                    50,
                    activation="relu",
                    input_shape=(time_steps, 1),
                    return_sequences=True,
                ),
                LSTM(50, activation="relu"),
                Dense(1),
            ]
        )
        lstm_model.compile(optimizer="adam", loss="mse")
        lstm_model.fit(
            X_lstm,
            y_lstm,
            epochs=10,
            batch_size=32,
            verbose=1,
            callbacks=[EarlyStopping(patience=3)],
        )

        lstm_model_path = os.path.join(
            model_dir, f"lstm_model_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.h5"
        )
        save_model(lstm_model, lstm_model_path)
        logging.info(f"LSTM model saved at {lstm_model_path}")
    except Exception as e:
        logging.error(f"Error during model building and serialization: {e}")
        raise
