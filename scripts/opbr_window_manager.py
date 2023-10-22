#opbr_window_manager.py
from PIL import ImageGrab, Image
import subprocess
import os
import cv2
import numpy as np 
import time
import pyautogui
import threading
import matplotlib.pyplot as plt

def view_image(image, title="single image"):
    """
    Display a single image with the given title.
    """
    plt.figure(figsize=(10, 7))
    plt.title(title)
    plt.imshow(image)
    plt.axis("on")
    plt.show()

def view_images(image_list, title="multiple images"):
    """
    Display a list of images in a grid with the given title.
    """
    length = len(image_list)
    rows = int(np.ceil(length / 2))
    fig, axes = plt.subplots(rows, 2, figsize=(15, 8))
    for ax, image in zip(axes.ravel(), image_list):
        ax.imshow(image)
        ax.axis("off")

def get_titlebar_height():
    """
    Get the height of the window title bar on Linux.
    """
    titlebar_buffer = 23  # Default value
    try:
        command = "xprop -id $(xdotool getactivewindow) | grep FRAME"
        output = subprocess.check_output(command, shell=True, text=True) 
        output = output.split(",")
        titlebar_buffer = int(output[3])
        return titlebar_buffer
    except subprocess.CalledProcessError:
        return None

def all_window_info():    
    """
    Get information about all open windows including their names, IDs, positions, and dimensions.
    """
    titlebar_buffer = get_titlebar_height()
    parts = []
    window_info = []
    try:
        command = "wmctrl -lG"
        output = subprocess.check_output(command, shell=True, text=True)        
        lines = output.splitlines()
        for line in lines:
            parts = line.split()
            window_name = ' '.join(parts[7:])
            window_id = parts[0]
            x_cord = parts[2]
            y_cord = parts[3] - titlebar_buffer
            width = parts[4]
            height = parts[5]
            window_info.append([window_name, window_id, x_cord, y_cord, width, height])
        return window_info
    except subprocess.CalledProcessError:
        return None

def specific_window_info(window_name="V2105"):
    """
    Get information about a specific window with the given name.
    """
    try:
        command = f'wmctrl -lG | grep "{window_name}"'
        result = subprocess.check_output(command, shell=True, text=True).strip()
        if result:
            parts = result.split()
            return {
                "window_id": parts[0],
                "x": int(parts[2]),
                "y": int(parts[3]),
                "width": int(parts[4]),
                "height": int(parts[5]),
            }
        else:
            print(f"No window with the title '{window_name}' found.")
            return None
    except subprocess.CalledProcessError:
        return None

def read_images_in_folder(folder_path):
    """
    Read images from a folder and return them as a list.
    """
    image_list = []
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_list.append(image)
    return image_list

def pyautogui_click(x, y, frame):
    """
    Perform a PyAutoGUI click at the specified coordinates (x, y).
    """
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.click(x, y)
    currentMouseX, currentMouseY = pyautogui.position()

def screenshot_pygui(screen_name, screenshot_path):
    """
    Capture a screenshot of a specific window using PyAutoGUI and save it to the specified path.
    """
    titlebar_buffer = get_titlebar_height()
    if titlebar_buffer is None:
        titlebar_buffer = 23  # Default Linux titlebar height
    screenshot = None
    win_info = specific_window_info(screen_name)
    if win_info:
        try:
            subprocess.run(["xdotool", "windowactivate", win_info["window_id"]])
            time.sleep(1.5)
            screenshot = pyautogui.screenshot(region=(win_info["x"], win_info["y"] - titlebar_buffer, win_info["width"], win_info["height"]))
            screenshot = np.array(screenshot)
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
            cv2.imwrite(screenshot_path, screenshot)
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
    else:
        print(f"No window with the title '{screen_name}' found.")
    return screenshot
