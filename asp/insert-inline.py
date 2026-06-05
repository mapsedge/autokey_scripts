#Enter script code
winTitle = window.get_active_title()

if '.asp' in winTitle:

    keyboard.send_keys("<ctrl>+x")
    time.sleep(.2)
    selText = clipboard.get_clipboard()
    time.sleep(.2)
    keyboard.send_keys("\" & ")
    keyboard.send_keys("<ctrl>+v")
    time.sleep(.2)
    keyboard.send_keys(" & \"")