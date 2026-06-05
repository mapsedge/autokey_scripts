import mapsedge_save

def getLabel():
    secs = str(time.time())
    return secs[-6:]

active_title = window.get_active_title()

label = getLabel()


if '.asp' in active_title:
    keyboard.send_keys("writeout \"[" + label + "] \" & now, 2")

if '.php' in active_title:
    clipboard.fill_clipboard('die("[' + label + '] " . date("Y/m/d H:i:s"));')
    time.sleep(1)
    keyboard.send_keys("<ctrl>+v")

if '.js' in active_title:
    clipboard.fill_clipboard('console.log("[' + label + ']", new Date().toString("yyyy-MM-dd HH:mm"));')
    time.sleep(.5)
    keyboard.send_keys("<ctrl>+v")

# mapsedge_save.doSave(keyboard, time, window)
