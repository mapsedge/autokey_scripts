from datetime import datetime
import time
# import keyboard

t = datetime.now()
f = t.strftime("%Y-%m-%d %H;%M")

# Enter script code
time.sleep(1)
keyboard.send_keys("<ctrl>+c")
time.sleep(0.5)
keyboard.send_keys("<ctrl>+v")

if window.wait_for_exist('Confirm to replace files|File Already Exists', 5):
	time.sleep(0.5)
	keyboard.send_keys("<home>")
	time.sleep(0.2)
	keyboard.send_keys(".${" + f + "}")
	time.sleep(0.2)
	keyboard.send_keys("<enter>")
