
#Enter script code
keyboard.send_keys("<ctrl>+s")
time.sleep(.5)
mouse.move_cursor(2100, 100)
keyboard.send_keys("<alt>+n")
time.sleep(.5)
count = 0
while (count < 11):
    count = count + 1
    keyboard.send_keys("<up>")
    time.sleep(.02)

time.sleep(.3)
keyboard.send_keys("<right>")       

time.sleep(.3)

count = 0
while (count < 7):
    count = count + 1
    keyboard.send_keys("<down>")
    time.sleep(.02)

time.sleep(.3)
keyboard.send_keys("<enter>")

