import unittest
from app import app

class TestClassifyEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_classify_low(self):
        response = self.client.get("/classify?value=25")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"value": 25, "status": "low"})

    def test_classify_high(self):
        response = self.client.get("/classify?value=120")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"value": 120, "status": "high"})

    def test_invalid_input(self):
        response = self.client.get("/classify?value=abc")
        self.assertEqual(response.status_code, 400)

    def test_missing_value(self):
        response = self.client.get("/classify")
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
