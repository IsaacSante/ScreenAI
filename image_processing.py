# Filename: image_processing.py

import logging
import cv2

def preprocess_image(image_path, processed_image_path='processed.png'):
    """
    Preprocess the image to enhance text recognition or visual clarity.

    Parameters:
        image_path (str): The path to the input image to preprocess.
        processed_image_path (str): The path to save the processed image.

    Returns:
        str: The path to the processed image if successful, else None.
    """
    logging.debug(f"Preprocessing image: {image_path}")
    # Read image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        logging.error(f"Failed to read image from {image_path}")
        return None
    # Convert to grayscale (optional)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply thresholding (optional)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    # Save the processed image
    cv2.imwrite(processed_image_path, thresh)
    logging.debug(f"Processed image saved to: {processed_image_path}")
    return processed_image_path
