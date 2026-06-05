#Enter script code
keyboard.send_keys("<ctrl>+s")
time.sleep(.5)

mouse.move_cursor(2100, 100)
keyboard.send_keys("<alt>+n")
time.sleep(.5)
count = 1
while (count < 12):
    count = count + 1
    keyboard.send_keys("<up>")
    time.sleep(.1)
keyboard.send_keys("<right>")
time.sleep(.5)

keyboard.send_keys("<up>")
time.sleep(.5)
keyboard.send_keys("<right>")

time.sleep(.5)
count = 0
while (count < 3):
    count = count + 1
    keyboard.send_keys("<up>")
    time.sleep(.1)
keyboard.send_keys("<enter>")
