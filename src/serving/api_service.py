from flask import Flask, request, jsonify
import joblib
import numpy as np
from tensorflow.keras.models import load_model
import os
import logging

app = Flask(__name__)


def load_latest_model(model_dir, model_type):
    """
    Load the latest serialized model from the given directory.
    """
    files = [f for f in os.listdir(model_dir) if model_type in f]
    latest_model = max(
        files, key=lambda f: os.path.getctime(os.path.join(model_dir, f))
    )
    model_path = os.path.join(model_dir, latest_model)
    if model_type == "rf_model":
        return joblib.load(model_path)
    elif model_type == "lstm_model":
        return load_model(model_path)
    return None


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        logging.info("Received prediction request.")
        data = request.json
        model_type = data.get("model_type", "rf_model")
        features = np.array(data["features"]).reshape(1, -1)

        if model_type == "rf_model":
            model = load_latest_model("models", "rf_model")
            prediction = model.predict(features)
        elif model_type == "lstm_model":
            model = load_latest_model("models", "lstm_model")
            features = features.reshape((features.shape[0], features.shape[1], 1))
            prediction = model.predict(features)
        else:
            logging.warning("Invalid model type specified.")
            return jsonify({"error": "Invalid model type specified"}), 400

        logging.info(f"Prediction successful: {prediction}")
        return jsonify({"prediction": float(prediction[0])})
    except Exception as e:
        logging.error(f"Error in prediction: {e}")
        return jsonify({"error": str(e)}), 500


def start_api_server(model_dir):
    """
    Start the Flask API server.
    """
    global MODEL_DIR
    MODEL_DIR = model_dir
    app.run(host="0.0.0.0", port=5000, debug=False)
