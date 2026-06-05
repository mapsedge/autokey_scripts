# Enter script code
time.sleep(.5)
keyboard.send_keys("<ctrl>+x")
time.sleep(.1)
#keyboard.send_keys("<!-- @")
#time.sleep(.1)
#keyboard.send_keys("<ctrl>+v")
#time.sleep(.1)
#keyboard.send_keys("@ ")

tag = clipboard.get_clipboard()
nextTag = "<!-- @" + tag + "@ -->"
clipboard.fill_clipboard(nextTag)
time.sleep(.5)
keyboard.send_keys("<ctrl>+v")

