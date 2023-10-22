# keyboard_listener.py
from pynput.keyboard import Listener
import threading
import psutil
import time
from dotenv import load_dotenv
import os
load_dotenv()

# Title of the scrcpy window to be closed
WINDOW_TITLE = os.getenv("WINDOW_TITLE")
END_KEY = os.getenv("END_KEY")


def close_scrcpy_window(window_title=WINDOW_TITLE):
    """
    Close the scrcpy window with the specified title.

    Args:
        window_title (str): The title of the scrcpy window to be closed.

    Returns:
        None
    """
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            process_info = proc.info
            process_cmdline = " ".join(process_info['cmdline'])
            if "scrcpy" in process_cmdline and window_title in process_cmdline:
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def on_press(key):
    """
    Handle key press events.

    Args:
        key (str): The key that was pressed.

    Returns:
        None
    """
    try:
        if key.char == END_KEY:
            print("M key pressed, terminating the OPBR-BOT...")
            close_scrcpy_window(WINDOW_TITLE)
            time.sleep(2)
            loop_flag = False  # Note: Make sure loop_flag is defined and accessible
    except AttributeError:
        pass

def start_listener():
    """
    Create and start a keyboard listener thread.

    Returns:
        threading.Thread: The listener thread.
    """
    return threading.Thread(target=lambda: Listener(on_press=on_press).start())
