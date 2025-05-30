#Enter script code
#keyboard.send_keys("<ctrl>+k")
time.sleep(.5)
engine.run_script("params")

if window.wait_for_exist('Embroidery Params',10):
	time.sleep(.3)
	mouse.click_absolute(2073, 56, 1)
	time.sleep(.3)
	mouse.click_absolute(2040, 181, 1)
	time.sleep(.3)
	mouse.click_absolute(2385, 373, 1)
	keyboard.send_keys("<tab>")
	time.sleep(.3)
	keyboard.send_keys("<tab>")
	time.sleep(.3)
	keyboard.send_keys("10")
	time.sleep(.3)
	for _ in range(41):
		keyboard.send_keys("<tab>")
	for _ in range(4):
		keyboard.send_keys("<down>")
	time.sleep(.3)
	mouse.scroll_down(12)
	time.sleep(8)
	mouse.click_absolute(2553, 1037, 1)
