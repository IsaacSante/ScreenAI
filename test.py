# Filename: test.py

import os
import logging
import openai
import base64
from pathlib import Path
from PIL import Image
import io
import traceback

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)

def test_openai_api_with_image(image_path):
    logging.debug("Testing OpenAI API with an image")

    detail_level = 'high'  # Options: 'low', 'high', 'auto'

    # Read, resize, and encode the image
    try:
        img = Image.open(image_path)

        # Resize the image based on desired detail level
        if detail_level == 'low':
            img = img.resize((512, 512))
        elif detail_level == 'high':
            # Resize short side to 768px while maintaining aspect ratio
            short_side = min(img.size)
            scaling_factor = 768 / short_side
            new_size = (int(img.size[0] * scaling_factor), int(img.size[1] * scaling_factor))
            img = img.resize(new_size)
        else:
            # For 'auto' or any other value, do not resize
            pass

        # Save to a bytes buffer
        buffer = io.BytesIO()
        img_format = img.format if img.format else 'PNG'
        img.save(buffer, format=img_format)
        img_bytes = buffer.getvalue()
        img_b64 = base64.b64encode(img_bytes).decode("utf-8")
        img_type = img_format.lower()

        # Create the data URL
        image_data_url = f"data:image/{img_type};base64,{img_b64}"
    except Exception as e:
        logging.error(f"Error processing image {image_path}: {e}")
        logging.debug(traceback.format_exc())
        return

    # Prepare the messages with the image
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_data_url,
                        "detail": detail_level
                    }
                }
            ]
        }
    ]

    try:
        # Send a request to the GPT-4 model with vision capabilities
        response = openai.ChatCompletion.create(
            model="gpt-4-vision",
            messages=messages,
            max_tokens=300
        )

        # Extract the assistant's reply
        reply = response.choices[0].message.get('content', '').strip()
        logging.debug(f"AI reply: {reply}")
        print(f"\nAssistant's response:\n{reply}")

    except openai.error.OpenAIError as e:
        logging.error(f"Error communicating with OpenAI API: {e}")
        logging.debug(traceback.format_exc())

if __name__ == "__main__":
    # Update the image path to point to a valid image file
    test_image_path = 'screenshot.png'  # Or any valid image file path
    test_openai_api_with_image(test_image_path)
