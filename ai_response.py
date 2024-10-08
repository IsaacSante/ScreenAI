# Filename: ai_response.py

import os
import logging
import base64
import io
import traceback
from pathlib import Path

from PIL import Image
from dotenv import load_dotenv  # For loading environment variables from .env
from openai import OpenAI  # Import the OpenAI client

# Load environment variables from .env file
load_dotenv()

# Load your OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Ensure the API key is loaded
if not api_key:
    raise ValueError("Please set your OPENAI_API_KEY in the .env file")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
)

def generate_ai_response_with_image(image_path):
    logging.debug("Generating AI response using image")

    detail_level = 'high'  # Options: 'low', 'high', 'auto'

    # Read, resize, and encode the image
    try:
        img = Image.open(image_path)

        # Resize the image based on desired detail level
        if detail_level == 'low':
            img = img.resize((512, 512))
        elif detail_level == 'high':
            # Resize logic for high detail
            max_short_side = 768
            max_long_side = 2000
            width, height = img.size
            scaling_factor = min(
                max_short_side / min(width, height),
                max_long_side / max(width, height)
            )
            new_size = (
                int(width * scaling_factor),
                int(height * scaling_factor)
            )
            img = img.resize(new_size)
        # No resize needed for 'auto' option

        # Save to a bytes buffer
        buffer = io.BytesIO()
        img_format = img.format if img.format else 'PNG'
        img.save(buffer, format=img_format)
        img_bytes = buffer.getvalue()
        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        img_type = img_format.lower()

        # Create the data URL
        image_data_url = f"data:image/{img_type};base64,{img_b64}"
    except Exception as e:
        logging.error(f"Error processing image {image_path}: {e}")
        logging.debug(traceback.format_exc())
        return None

    # Prepare the messages with the image
    messages = [
        {
            "role": "system",
            "content": (
                "You are participating in the following conversation. Respond as if you are replying to the last message, "
                "in a natural and conversational manner. Your response should be appropriate, concise, and in first person singular. "
                "Do not mention that you are an AI language model or provide any analysis; just continue the conversation."
            )
        },
        {
            "role": "user",
            "content": [
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
        # Use the OpenAI client to create chat completion
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Ensure you're using a model that supports vision capabilities
            messages=messages,
            max_tokens=300
        )

        # Extract the assistant's reply
        reply = response.choices[0].message.content.strip()
        logging.debug(f"AI reply: {reply}")
        return reply
    except Exception as e:
        logging.error(f"Error generating AI response: {e}")
        logging.debug(traceback.format_exc())
        return None
