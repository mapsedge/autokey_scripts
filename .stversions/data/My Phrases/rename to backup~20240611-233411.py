from datetime import datetime
t = datetime.now()
f = t.strftime("%Y-%m-%d %H;%M")
#Enter script code
time.sleep(1)
keyboard.send_keys("<ctrl>+c")
time.sleep(.2)
keyboard.send_keys("<ctrl>+v")
time.sleep(.2)

keepgoing = True

while keepgoing:
    keepgoing = window.wait_for_exist("Confirm to replace files", 5)
    if keepgoing:
        time.sleep(1)
        keyboard.send_keys("<home>")
        time.sleep(.2)
        keyboard.send_keys("${" + f + "}")
        time.sleep(.2)
        keyboard.send_keys("<enter>")

dialog.info_dialog('done')