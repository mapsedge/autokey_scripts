
#renames the file in place without making a copy
from datetime import datetime

d = datetime.now().strftime("%Y-%m-%d %H;%M")
clipboard.fill_clipboard(".${" + d + "} ")
time.sleep(.2)
keyboard.send_keys("<f2>")
time.sleep(.2)
keyboard.send_keys("<end>")
time.sleep(.2)
keyboard.send_keys("<home>")
time.sleep(.2)
keyboard.send_keys("<ctrl>+v")
time.sleep(.2)
keyboard.send_keys("<enter>")



