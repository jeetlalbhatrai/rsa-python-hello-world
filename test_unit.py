import unittest
from classify import classify_value

class TestClassifyFunction(unittest.TestCase):
    def test_low(self):
        self.assertEqual(classify_value(10), {"value": 10, "status": "low"})

    def test_high(self):
        self.assertEqual(classify_value(150), {"value": 150, "status": "high"})

    def test_edge(self):
        self.assertEqual(classify_value(100), {"value": 100, "status": "high"})

if __name__ == "__main__":
    unittest.main()
