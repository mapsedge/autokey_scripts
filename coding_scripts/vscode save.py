# Enter script code

keyboard.send_keys("<ctrl>+s")

#start_time = time.time()
#if (time.time()-start_time < 0.9):
#    time.sleep(0.2)
time.sleep(.7)
window.activate("File Changed")
time.sleep(0.1)
active_title = window.get_active_title()
if (active_title == "File Changed"):
    keyboard.send_key("<enter>")

time.sleep(.7)
window.activate("File Already Exists")
time.sleep(0.1)
active_title = window.get_active_title()
if (active_title == "File Already Exists"):
    keyboard.send_keys("<alt>+o")


