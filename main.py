# Filename: main.py

import logging
import sys
from dotenv import load_dotenv
from screen_capture import capture_region_interactive
from ai_response import generate_ai_response_with_image
from ui_automation import type_and_send_message  # Removed activate_application import
from image_processing import preprocess_image

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(),
    ]
)

# Platform check (ensure the script is running on macOS)
if sys.platform != 'darwin':
    logging.error("This application is designed for macOS and may not function correctly on other operating systems.")
    sys.exit(1)

def main():
    logging.info("Starting the application")

    logging.info("Please select a region of the screen to capture")
    screenshot_path = 'screenshot.png'
    capture_region_interactive(screenshot_path)

    # Optionally preprocess the image
    processed_image = preprocess_image(screenshot_path)
    if processed_image:
        # Generate AI response using the processed image
        reply = generate_ai_response_with_image(processed_image)
    else:
        logging.error("Failed to preprocess image.")
        return

    if reply:
        logging.info(f"AI Reply: {reply}")

        # Type out the message in Messages app and prompt before sending
        type_and_send_message(reply, prompt_before_sending=True)
    else:
        logging.error("Failed to generate AI reply.")

if __name__ == "__main__":
    main()
