"""
opbr_color_module.py

This module defines color codes for text output in the terminal.

Usage:
    from color_module import RED, GREEN, YELLOW, BLUE, MAGENTA, LIGHTGRAY, WHITE, print_colored

Example usage:
    print_colored("This is red text.", RED)
"""

# Default text color (Cyan)
RESET = "\033[0m"

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
LIGHTGRAY = "\033[97m"
WHITE = "\033[97m"

# Additional color codes
PINK = "\033[38;5;206m"  # Pink (may vary depending on terminal)
ORANGE = "\033[38;5;202m"  # Orange (may vary depending on terminal)
VIOLET = "\033[38;5;165m"  # Violet (may vary depending on terminal)
GOLD = "\033[38;5;220m"  # Gold (may vary depending on terminal)
LAVENDER = "\033[38;5;183m"  # Lavender (may vary depending on terminal)
TEAL = "\033[38;5;037m"  # Teal (may vary depending on terminal)

def print_colored(text, color):
    """
    Print colored text to the terminal.

    Args:
        text (str): The text to be printed.
        color (str): The color code to apply to the text.

    Example:
        print_colored("This is red text.", RED)
    """
    print(f"{color}{text}{RESET}")

# Example print statements
if __name__ == "__main__":
    print_colored("This is red text.", RED)
    print_colored("This is green text.", GREEN)
    print_colored("This is yellow text.", YELLOW)
    print_colored("This is blue text.", BLUE)
    print_colored("This is magenta text.", MAGENTA)
    print_colored("This is light gray text.", LIGHTGRAY)
    print_colored("This is white text.", WHITE)
    print_colored("This is pink text.", PINK)
    print_colored("This is orange text.", ORANGE)
    print_colored("This is violet text.", VIOLET)
    print_colored("This is gold text.", GOLD)
    print_colored("This is lavender text.", LAVENDER)
    print_colored("This is teal text.", TEAL)
