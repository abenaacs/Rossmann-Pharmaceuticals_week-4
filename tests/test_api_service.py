import unittest
from src.serving.api_service import app


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_rf_model_prediction(self):
        response = self.app.post(
            "/predict",
            json={
                "model_type": "rf_model",
                "features": [1, 15, 7, 2023, 2, 0],  # Sample data
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.get_json())

    def test_invalid_model_type(self):
        response = self.app.post(
            "/predict",
            json={"model_type": "invalid_model", "features": [1, 15, 7, 2023, 2, 0]},
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
