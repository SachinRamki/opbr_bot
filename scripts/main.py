import cv2
import numpy as np
import threading
import time
from ultralytics import YOLO
import pyautogui
from dotenv import load_dotenv
import os


import opbr_window_manager as gw
from opbr_keyboard_listener import start_listener, close_scrcpy_window
from opbr_scrcpy_manager import start_scrcpy, is_scrcpy_active
import opbr_mouseclicks as mc
import opbr_colour_module as cm

load_dotenv()

# Constants
OFFSET_H_PX = gw.get_titlebar_height()
SCREEN_ID = os.getenv("SCREEN_ID")
CIRCLE_PATH = os.getenv("CIRCLE_PATH")
SCREENSHOT_PATH = os.getenv("SCREENSHOT_PATH")
MODEL_PATH = os.getenv("MODEL_PATH")

# Global variables
start_time = time.time()
loop_flag = True

def bot_logic():
    """
    Main bot logic function for processing frames, detecting classes, and automating clicks.
    """
    global loop_flag
    counter = 0
    class_cache_buffer = []
    print(f"Initializing background processes. Please wait...")
    time.sleep(1.5)
    while loop_flag:
        if is_scrcpy_active():
            frame = gw.screenshot_pygui(SCREEN_ID, SCREENSHOT_PATH + str(time.time()) + ".jpeg")

            if frame is not None and np.any(frame):
                results = opbr_model(frame, verbose=False)

                c_id, mx, my, classes = mc.get_result_info(results, view=False)  # Set view=False for no output images

                if c_id is not None:
                    print(f"Processing counter: {counter}, {cm.PINK}class ID: {c_id} -> {classes[c_id]}{cm.RESET}")

                    class_cache_buffer, loop_flag = mc.automate_clicks(c_id, mx, my + OFFSET_H_PX, classes,
                                                                       class_cache_buffer)
                    counter += 1
                    class_cache_buffer = mc.check_cache(counter, class_cache_buffer)
                else:
                    print("No class detected. Make sure the game is visible.")
                    class_cache_buffer.append(None)
                    class_cache_buffer = mc.check_cache(counter, class_cache_buffer)
                    time.sleep(1)
            else:
                print("WARNING! No proper input or frame capture failed.")
                break

            if not loop_flag:
                break
        else:
            print(f"{cm.RED}Screen mirror has been stopped.{cm.RESET}")
            break

if __name__ == "__main__":
    try:
        # Create and start the listener thread
        listener_thread = start_listener()
        listener_thread.start()
        print(f"{cm.RED}Screen mirror is now active.{cm.RESET}")

        # Create a thread for running scrcpy
        scrcpy_thread = threading.Thread(target=start_scrcpy)
        scrcpy_thread.start()
        time.sleep(4)

        # Initialize YOLO model
        opbr_model = YOLO(MODEL_PATH)
        print("OPBR-Bot is now running. To stop the bot, press the 'M' key.")

        # Run the main bot logic in the main thread
        bot_logic()
        print("Terminating background processes. Please wait...")

        # Close the scrcpy window
        close_scrcpy_window()

        # Wait for the scrcpy thread to finish
        scrcpy_thread.join()

        # Wait for the listener thread to finish
        listener_thread.join()
        time.sleep(3)

        print(f"Total execution time: {((time.time() - start_time) / 60):.2f} minutes...")
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (e.g., user presses Ctrl+C)
        print("Ctrl+C pressed, terminating the BOT")
