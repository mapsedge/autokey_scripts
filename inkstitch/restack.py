#Enter script code
data = [
	("<ctrl>+s", 1, 1),
	("<alt>+n", 1, .2),
	("<up>", 11, .2),
	("<right>", 1, .2),
	("<down>", 3, .2),
	("<right>", 1, .2),
	("<down>", 3, .2),
	("<enter>", 1, .01),
]
time.sleep(1)
mouse.move_cursor(2100, 100)
for string, number, pause in data:
	for _ in range(number):
		keyboard.send_keys(string)
		time.sleep(pause)
