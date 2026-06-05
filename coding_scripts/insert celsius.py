import re
import mapsedge_save


def cutSelection():
    keyboard.send_keys("<shift>+<ctrl>+<left>")
    time.sleep(.2)
    keyboard.send_keys("<shift>+<ctrl>+<left>")
    time.sleep(.2)
    keyboard.send_keys("<ctrl>+c")
    time.sleep(.2)
    selText = clipboard.get_clipboard()
    time.sleep(.2)
    return selText

def main():
    # Enter script code
    active_title = window.get_active_title()
    # dialog.info_dialog("active title", active_title)
    if 'Post an Entry' in active_title:
    
        selText = cutSelection()

        # Extract the numbers from selText
        match = re.search(r'\d+', selText)
        if match:
            old_value = int(match.group(0))
            
            # Calculate Celsius
            new_value = round((old_value - 32) * 5 / 9)

            # Format the new value
            output = f"° ({new_value:.1f}°C)"
            
            # Move to the end of the line and output the result
            keyboard.send_keys('<end>')
            keyboard.send_keys(output)
        exit

    else:
        keyboard.send_keys("°")


main()
