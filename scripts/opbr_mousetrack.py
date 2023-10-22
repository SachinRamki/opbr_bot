import sys
import tty
import termios
import pyautogui

def monitor_keypress():
    """
    Monitor key presses and display the mouse position when 's' is pressed.
    
    Press 'q' to exit the monitoring.
    """
    print("Monitoring key presses. Press 'q' to exit.")
    original_settings = termios.tcgetattr(sys.stdin)  # Get original terminal settings
    try:
        tty.setcbreak(sys.stdin.fileno())  # Set terminal to cbreak mode
        while True:
            key = sys.stdin.read(1)
            if key == 'q':
                print("Exiting...")
                break
            elif key == 's':
                print(f"Mouse Position: {pyautogui.position()}")
            print(f"Key pressed: {key}")

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings) 

if __name__ == "__main__":
    monitor_keypress()
