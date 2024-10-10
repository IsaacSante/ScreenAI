# ScreenAI Assistant

**Version:** 1.0

## Overview

ScreenAI Assistant is a macOS application that bridges user interactions with AI capabilities directly from the desktop environment. It allows you to capture any region of your screen, process the image, and generate AI-driven responses or actions based on the content. The primary use case demonstrated is capturing a screen snippet and automating a response in the Messages app, but the architecture is designed to expand across various applications and functionalities on your operating system.

## Features

- **Interactive Screen Capture:** Select any region of your screen for processing via an intuitive interface.
- **Image Preprocessing:** Enhance captured images to improve AI interpretation using techniques like resizing and thresholding.
- **AI Integration:** Utilize advanced AI models (e.g., GPT-4 with vision capabilities) to generate context-aware responses from images.
- **Automated Messaging:** Automatically type and send AI-generated messages through the Messages app with optional user prompts before sending.
- **Extensible Automation Framework:** Built to expand beyond messaging, allowing automated interactions across multiple applications and system functionalities.

## Technical Details

- **Language & Libraries:**
  - Python 3
  - OpenAI API (for AI interactions)
  - Pillow (PIL) and OpenCV (for image processing)
  - PyAutoGUI (for UI automation)
  - AppleScript via `osascript` (for macOS-specific actions)
- **Modular Architecture:**
  - **`screen_capture.py`:** Handles interactive screen region selection using macOS's native `screencapture` utility.
  - **`image_processing.py`:** Processes images to enhance AI readability (grayscale conversion, thresholding, resizing).
  - **`ai_response.py`:** Encodes images and communicates with the OpenAI API to generate responses based on image content.
  - **`ui_automation.py`:** Automates typing and sending messages, with the potential to control any application.
- **Extensibility:**
  - The system is designed to be modular, making it straightforward to integrate additional applications and user actions.
  - Future implementations could include automating email responses, interacting with web browsers, or controlling system settings based on AI interpretations.

## Potential Expansions

- **Universal Application Control:** Extend capture and automation capabilities to interact with any application on your computer, not just the Messages app.
- **Diverse User Actions:** Incorporate a wider range of actions such as clicking, dragging, scrolling, and application-specific commands.
- **Cross-Platform Support:** Adapt the tool for other operating systems like Windows and Linux, leveraging platform-specific tools.
- **Customized AI Models:** Allow users to select from various AI models or services to fit different use cases and performance needs.
- **Contextual Automation Scripts:** Develop scripts that can make system-wide changes or complex sequences of actions based on AI analysis.

## Usage

1. **Setup:**
   - Ensure macOS is your operating system (designed specifically for macOS).
   - Install Python 3 and required dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Set your OpenAI API key in a `.env` file:

     ```env
     OPENAI_API_KEY=your_api_key_here
     ```

2. **Running the Application:**

   - Execute the main script:

     ```bash
     python main.py
     ```

   - Follow the on-screen prompts to select a screen region and process the AI response.
   - Optionally review the message before it's sent.

## Security Considerations

- **Privacy:** Be cautious of sensitive information when capturing screen regions. The images are processed and sent to an external AI service.
- **API Key Management:** Keep your OpenAI API key secure and do not share it.
- **Use Responsibly:** Ensure compliance with OpenAI's usage policies and any applicable laws or regulations when automating actions.

## Conclusion

ScreenAI Assistant showcases the integration of AI with desktop automation, providing a foundation that can be expanded to control various applications and system functionalities across your OS. This tool not only demonstrates proficiency in Python and macOS automation but also opens the door for innovative developments in AI-driven user interfaces.
