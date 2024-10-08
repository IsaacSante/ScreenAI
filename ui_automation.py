# Filename: ui_automation.py

import logging
import os
import time
import pyautogui

def activate_application(app_name):
    logging.debug(f"Activating application: {app_name}")
    try:
        result = os.system(f"osascript -e 'tell application \"{app_name}\" to activate'")
        if result != 0:
            logging.error(f"Failed to activate application {app_name}.")
        else:
            logging.debug(f"Application {app_name} activated")
    except Exception as e:
        logging.error(f"Error activating application {app_name}: {e}")

def type_and_send_message(message, prompt_before_sending=False):
    logging.debug("Entering type_and_send_message function.")
    try:
        # Prompt user to ensure the Messages input box is focused
        input("Ensure the Messages input box is focused and press Enter to continue...")

        # After the user presses Enter, re-activate Messages app
        activate_application("Messages")
        time.sleep(0.5)

        logging.debug("Messages app activated after terminal input.")

        # Type the message
        logging.debug(f"Typing message: {message}")
        pyautogui.write(message, interval=0.05)
        logging.debug("Message typing completed.")
        time.sleep(0.5)

        if prompt_before_sending:
            # Prompt in the terminal whether to send the message
            send = input("Do you want to send the message? (y/n): ").strip().lower()

            # Re-activate Messages app again
            activate_application("Messages")
            time.sleep(0.5)

            logging.debug(f"User response to send prompt: {send}")
            if send == 'y':
                # Press 'Enter' to send the message
                pyautogui.press('enter')
                logging.debug("Pressed 'Enter' to send the message.")
            else:
                logging.debug("User opted not to send the message.")
        else:
            # Press 'Enter' to send the message
            pyautogui.press('enter')
            logging.debug("Message sent without prompt.")
    except Exception as e:
        logging.error(f"Error typing and sending message: {e}")
        logging.debug(e, exc_info=True)
