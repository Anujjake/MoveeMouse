import pyautogui
import time

def move_mouse():
    # Get the current mouse position
    current_x, current_y = pyautogui.position()

    # Move the mouse cursor a bit (10 pixels to the right and 10 pixels down)
    new_x = current_x + 10
    new_y = current_y + 10
    pyautogui.moveTo(new_x, new_y, duration=0.25)

if __name__ == "__main__":
    try:
        while True:
            move_mouse()
            time.sleep(30)  # Wait for 30 seconds before the next move
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
