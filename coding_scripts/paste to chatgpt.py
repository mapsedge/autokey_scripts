#Enter script code

time.sleep(.5)
keyboard.send_keys("<ctrl>+c")
time.sleep(.1)
window.activate("Immurement definition")
time.sleep(.2)
mouse.move_cursor(3023, 965)
time.sleep(.1)
mouse.click_relative_self(0, 0, 1)
time.sleep(.1)
keyboard.send_keys("<ctrl>+v")
time.sleep(.1)
keyboard.send_keys("<enter>")

