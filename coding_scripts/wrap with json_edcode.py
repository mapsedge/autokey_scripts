# Prompt the user for input
choice = dialog.input_dialog("Input", "Choose (d)ecode or (e)ncode:")
choice = choice[1].lower()

# Get the currently selected text
selected_text = clipboard.get_selection()

# Define the result based on the user's choice
if choice == 'd':
    result = f'json_decode({selected_text})'
elif choice == 'e':
    result = f'json_encode({selected_text})'
else:
    result = 'Invalid choice. Please choose (d)ecode or (e)ncode.'

# Replace the selected text with the result
clipboard.fill_clipboard(result)  # Set the result into the clipboard
keyboard.send_keys("<ctrl>+v")  # Paste the result where the cursor is
