#Enter script code
keyboard.send_keys("<ctrl>+x")
time.sleep(.2)
var1 = clipboard.get_clipboard()
time.sleep(.2)
var2 = "\"" + var1 + "\""
clipboard.fill_clipboard(var2)
time.sleep(.2)
keyboard.send_keys("<ctrl>+v")
