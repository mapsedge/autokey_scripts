from datetime import datetime
t = datetime.now()
f = t.strftime("%Y-%m-%d %H;%M")
#Enter script code
time.sleep(1)
keyboard.send_keys("<f2>")
time.sleep(.2)
keyboard.send_keys("<home>")
time.sleep(.2)
keyboard.send_keys("${" + f + "}")
time.sleep(.2)
keyboard.send_keys("<enter>")
