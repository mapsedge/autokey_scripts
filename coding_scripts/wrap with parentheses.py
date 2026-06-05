#Enter script code
time.sleep(.5)
keyboard.send_keys("<ctrl>+x")
time.sleep(.2)
var1 = clipboard.get_clipboard()
var2 = "(" + var1 + ")"
clipboard.fill_clipboard(var2)
time.sleep(.2)
keyboard.send_keys("<ctrl>+v")
