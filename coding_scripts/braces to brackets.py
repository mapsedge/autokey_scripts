import re

# Get the currently selected text
keyboard.send_keys('<ctrl>+c')
time.sleep(.1)
selected_text = clipboard.get_clipboard()
time.sleep(.1)
modified_text = selected_text.replace("{", "[").replace("}", "]")
time.sleep(.1)
# Update the clipboard with the modified text
clipboard.fill_clipboard(modified_text)
time.sleep(.1)
# Optionally, notify the user
keyboard.send_keys('<ctrl>+v')  # Replace selection with modified text if desired
