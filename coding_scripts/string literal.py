#Enter script code

keyboard.send_keys("<ctrl>+x")
time.sleep(.4)
x = clipboard.get_clipboard()
time.sleep(.4)
clipboard.fill_clipboard("${" + x + "}")
time.sleep(.4)
keyboard.send_keys("<ctrl>+v")