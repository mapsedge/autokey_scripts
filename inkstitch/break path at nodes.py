import pyautogui
import subprocess
import time
import os

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, '../img/pygui-break-nodes.png')

def show_notification(title, message):
    """Show a system tray notification using notify-send."""
    try:
        subprocess.run([
            'notify-send',
            title,
            message,
            '-u', 'normal',
            '-t', '3000'
        ], check=False)
    except Exception as e:
        print(f"Notification failed: {e}")

try:
    # Find the button using image recognition
    button_center = pyautogui.locateCenterOnScreen(img_path)

    if button_center is None:
        show_notification(
            "Break Path at Nodes",
            "Button not found on screen. Is Inkscape window visible?"
        )
    else:
        # Move mouse smoothly to button center (0.3 sec for quick but smooth movement)
        pyautogui.moveTo(button_center[0], button_center[1], duration=0.3)

        # Wait 500ms before clicking
        time.sleep(0.5)

        # Click the button
        pyautogui.click()

        time.sleep(0.75)

        # Send keyboard shortcut for the actual operation
        keyboard.send_keys("<shift>+<ctrl>+k")

except Exception as e:
    show_notification(
        "Break Path at Nodes - Error",
        f"Script failed: {str(e)}"
    )
