# Filename: screen_capture.py

import logging
import subprocess

def capture_region_interactive(save_path='screenshot.png'):
    logging.debug("Starting interactive region selection using macOS screencapture tool.")

    try:
        # Call macOS's screencapture utility with interactive mode
        subprocess.run(['screencapture', '-i', save_path], check=True)
        logging.debug(f"Region capture successful, saved to {save_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error capturing screen region: {e}")
        return None

    return save_path
