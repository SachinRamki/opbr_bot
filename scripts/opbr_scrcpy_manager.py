# scrcpy_manager.py
import subprocess
import time
import psutil
from opbr_keyboard_listener import close_scrcpy_window

# Global variable to track the scrcpy process
scrcpy_process = None

def get_screen_resolution():
    """
    Get the screen resolution of the scrcpy window.

    Returns:
        tuple: A tuple containing the width and height of the screen resolution.
    """
    resolution_command = 'wmctrl -lG | grep V2105'
    try:
        result = subprocess.run(
            resolution_command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        output = result.stdout
        parts = output.strip().split()  # Split by whitespace
        w = int(parts[4])
        h = int(parts[5])
        return w, h
    except subprocess.CalledProcessError:
        return None, None  # Return both values as None

def check_resolution():
    """
    Check if the screen resolution meets the requirements.

    Returns:
        bool: True if the resolution meets the requirements, False otherwise.
    """
    w, h = get_screen_resolution()
    if w is not None:
        if w != 1024 and w != 352:  # 1024 in landscape and 352 in portrait
            return True
    else:
        return False

def start_scrcpy():
    """
    Start the scrcpy process and handle resolution checks.

    Returns:
        None
    """
    global scrcpy_process

    scrcpy_command = "scrcpy --window-borderless --window-x=0 --window-y=0 --max-size 1024 --stay-awake --window-title=V2105 --disable-screensaver --always-on-top --record file.mp4"

    scrcpy_process = subprocess.Popen(scrcpy_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Check if the resolution meets the requirements
    time.sleep(3)

    if check_resolution():
        print("Screen size less than 1024, doesn't match BOT requirement, RESTARTING...")
        close_scrcpy_window()
        start_scrcpy()

    try:
        while scrcpy_process.poll() is None:
            pass

    except KeyboardInterrupt:
        print("Ctrl+C pressed, terminating the BOT")

    finally:
        if scrcpy_process.poll() is None:
            print("Terminating scrcpy process...")
            scrcpy_process.terminate()
            scrcpy_process.wait()

    time.sleep(0.5)

def is_scrcpy_active():
    """
    Check if scrcpy is active.

    Returns:
        bool: True if scrcpy is active, False otherwise.
    """
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            process_info = process.info
            process_cmdline = " ".join(process_info['cmdline'])
            if "scrcpy" in process_cmdline:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if __name__ == "__main__":
    start_scrcpy()
