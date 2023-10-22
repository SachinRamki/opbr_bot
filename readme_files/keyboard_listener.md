## Documentation for `keyboard_listener.py`

### Overview

This Python script, `keyboard_listener.py`, is designed to monitor keyboard input and take specific actions when a predefined key is pressed. It uses the `pynput` library to listen for key press events and responds by closing a specific window with a given title. Additionally, it stops a designated process when a specific key is pressed.

### Dependencies

This script depends on the following Python libraries:

- `pynput`: Used for monitoring keyboard input.
- `threading`: Utilized to create a separate thread for keyboard input monitoring.
- `psutil`: Required for interacting with system processes to close a specific window.
- `time`: Used for introducing delays in the script.
- `dotenv`: Used for loading environment variables from a `.env` file.
- `os`: Provides access to operating system-specific functionality.

### Environment Variables

This script reads environment variables using the `dotenv` library to customize its behavior. The relevant environment variables are:

- `WINDOW_TITLE`: The title of the window that needs to be closed.
- `END_KEY`: The key that, when pressed, triggers the script's action.

Before running the script, make sure to define these environment variables in a `.env` file or through another method suitable for your environment.

### Functions

The script contains the following functions:

1. `close_scrcpy_window(window_title=WINDOW_TITLE)`

    This function closes the window with the specified title by terminating the associated process.

    - **Parameters**:
        - `window_title` (str): The title of the window to be closed. By default, it uses the value of the `WINDOW_TITLE` environment variable.

    - **Returns**:
        - None

2. `on_press(key)`

    This function is an event handler for key press events. It checks if a specific key is pressed, and if so, it takes action to close a window.

    - **Parameters**:
        - `key` (str): The key that was pressed.

    - **Returns**:
        - None

3. `start_listener()`

    This function creates and starts a separate thread for the keyboard listener.

    - **Returns**:
        - `threading.Thread`: The listener thread.

### Usage

To use this script, follow these steps:

1. Define the `WINDOW_TITLE` and `END_KEY` environment variables in a `.env` file or through your preferred method.

2. Import this script into your main application.

3. Call the `start_listener` function to initiate the keyboard listener.

4. The listener will be active, monitoring key presses. When the `END_KEY` is pressed, it will close the window with the title specified in `WINDOW_TITLE`.

### Important Note

Ensure that the `loop_flag` variable mentioned in the `on_press` function is defined and accessible within your application code. This variable is intended to control the termination of the script. When the `END_KEY` is pressed, it sets `loop_flag` to `False`, allowing your application to terminate gracefully if necessary.
