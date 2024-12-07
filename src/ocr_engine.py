import json
import os
from PIL import Image
import pytesseract

# Default Tesseract path (fallback)
DEFAULT_TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load configuration
try:
    with open('config.json') as config_file:
        config = json.load(config_file)
    tesseract_path = config.get('tesseract_cmd', DEFAULT_TESSERACT_PATH)
except FileNotFoundError:
    print("Error: 'config.json' not found. Please create it using 'config.example.json' as a template.")
    tesseract_path = DEFAULT_TESSERACT_PATH

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def extract_text(image_path):
    """
    Extracts text from the given image using Tesseract OCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: The extracted text.
    """
    try:
        if not os.path.exists(image_path):
            print(f"File not found: {image_path}")
            return ""

        print(f"File exists: {image_path}")
        print(f"File permissions: {oct(os.stat(image_path).st_mode)}")

        # Open the image
        image = Image.open(image_path)

        # Use custom Tesseract configuration
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(image, config=custom_config)
        print(f"Extracted Text:\n{text}")
        return text

    except Exception as e:
        print(f"Error in extract_text: {e}")
        return ""
