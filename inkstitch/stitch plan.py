#Enter script code
keyboard.send_keys("<ctrl>+s")
time.sleep(.5)

data = [
	("<alt>+n", 1, .5),
	("<up>", 11, .05),
	("<right>", 1, .05),
	("<up>", 1, .05),
	("<right>", 1, .05),
	("<up>", 2, .3),
	("<enter>", 1, 1),
	("<enter>", 1, 0),
]
time.sleep(1)
for string, number, pause in data:
	for _ in range(number):
		keyboard.send_keys(string)
		time.sleep(pause)
