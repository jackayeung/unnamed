import unittest
from src.ocr_engine import extract_text

class TestOCREngine(unittest.TestCase):
    def test_extract_text(self):
        sample_image = "data/images/sample.jpg"
        result = extract_text(sample_image)
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
