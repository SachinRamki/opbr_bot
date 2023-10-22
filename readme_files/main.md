# OPBR Bot Main Script

The OPBR Bot Main Script is the core of the bot that automates actions based on the detection of objects in the game screen. It utilizes the Ultralytics YOLO model for object detection, captures screenshots of the game, and performs automated clicks.

## Dependencies

The script has several dependencies, including:

- `cv2` (OpenCV) for image processing.
- `numpy` for numerical and array operations.
- `threading` for managing threads.
- `time` for time-related operations.
- `pyautogui` for automating mouse and keyboard inputs.
- `dotenv` for loading environment variables.
- Custom modules from the OPBR project, such as `opbr_window_manager`, `opbr_keyboard_listener`, `opbr_scrcpy_manager`, `opbr_mouseclicks`, and `opbr_colour_module`.

## Constants

- `OFFSET_H_PX`: The height offset in pixels to account for the window title bar.
- `SCREEN_ID`: The ID of the game screen to capture.
- `CIRCLE_PATH`: The path to the circle data (model weights).
- `SCREENSHOT_PATH`: The directory to save captured screenshots.
- `MODEL_PATH`: The path to the YOLO model for object detection.

## Global Variables

- `start_time`: Timestamp to record the start time of bot execution.
- `loop_flag`: A global flag to control the bot's main loop.

## Functions

### `bot_logic()`

Main bot logic function for processing frames, detecting classes, and automating clicks.

### `if __name__ == "__main__":`

The main entry point of the script. Initializes background processes, starts a listener thread, and runs the bot logic. Also handles keyboard interruptions to gracefully terminate the bot.

## Usage

The `main.py` script serves as the central component of the OPBR bot. It utilizes various custom modules to automate actions within a game, including object detection, mouse clicks, and handling scrcpy mirroring. To use the bot, make sure to configure the constants and dependencies correctly, such as setting the model path and game screen parameters.

## Terminating the Bot

To stop the bot, press the 'M' key, which will trigger the `if __name__ == "__main__":` block and gracefully terminate the bot, closing background processes, and ensuring a clean exit.

---

This documentation provides an overview of the main functionality and usage of the `main.py` script, which is responsible for running the OPBR bot, including object detection, mouse clicks, and game automation.
