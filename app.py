from flask import Flask, request, jsonify
import joblib
import tensorflow as tf
import pandas as pd
from src.data_preprocessing.data_preprocessor import DataPreprocessor

app = Flask(__name__)

# Load models
rf_model = joblib.load("models/rf_model_2025-01-13_23-38-40.pkl")

# Register the mse function explicitly
custom_objects = {"mse": tf.keras.losses.MeanSquaredError()}

# Load the LSTM model
lstm_model = tf.keras.models.load_model(
    "models/lstm_model_2025-01-14_00-24-09.h5", custom_objects=custom_objects
)


@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "API is running"})


@app.route("/predict-rf", methods=["POST"])
def predict_rf():
    data = request.get_json()
    input_data = pd.DataFrame(data)

    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess(input_data)

    # Drop unnecessary columns
    irrelevant_columns = ["Date", "DayOfWeek", "Id"]
    preprocessed_data = preprocessed_data.drop(
        irrelevant_columns, axis=1, errors="ignore"
    )

    # Align feature names
    training_features = rf_model.feature_names_in_
    preprocessed_data = preprocessed_data.reindex(
        columns=training_features, fill_value=0
    )

    # Make prediction
    prediction = rf_model.predict(preprocessed_data)
    return jsonify({"prediction": prediction.tolist()})


@app.route("/predict-lstm", methods=["POST"])
def predict_lstm():
    data = request.get_json()
    input_data = pd.DataFrame(data)

    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess(input_data)
    preprocessed_data.columns = [
        col.replace("Is_Weekend", "IsWeekend") for col in preprocessed_data.columns
    ]

    print(f"Preprocessed lstm data shape: {preprocessed_data.shape}")
    print(f"Preprocessed lstm data columns: {preprocessed_data.columns.tolist()}")

    prediction = lstm_model.predict(preprocessed_data)
    return jsonify({"prediction": prediction.tolist()})


if __name__ == "__main__":
    app.run(debug=True)
