import os
from src.ocr_engine import extract_text
from src.utils import save_transcript

def main():
    # Define the image name dynamically
    image_name = "TEST" 

    #WHY DOES IT WORK FOR THIS IMAGE BUT NOT THE OTHER ONE
    image_path = f"data/images/{image_name}.jpg"
    output_path = f"data/transcripts/{image_name}.txt"

    #check if image file exists before proceeding
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' does not exist.")
        return

    # Extract text and save transcript
    text = extract_text(image_path)
    save_transcript(output_path, text)

    print(f"Transcript saved to {output_path}")

if __name__ == "__main__":
    main()
