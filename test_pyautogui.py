import pyautogui
import time

input("Focus your cursor into the Messages input box and press Enter to continue...")

message = "This is a test message from PyAutoGUI."

pyautogui.write(message, interval=0.05)
time.sleep(0.5)
pyautogui.press('enter')
