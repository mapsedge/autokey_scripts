import mapsedge_save


def cutSelection():
    keyboard.send_keys("<end>")
    time.sleep(.2)
    keyboard.send_keys("<shift>+<home>")
    time.sleep(.2)
    keyboard.send_keys("<ctrl>+x")
    time.sleep(.2)
    selText = clipboard.get_clipboard()
    time.sleep(.2)
    return selText

def getLabel():
    secs = str(time.time())
    return secs[-6:]

winTitle = window.get_active_title()
label = getLabel()
selText = cutSelection()

selText2 = selText.replace("\"", "\\\"")
selText_php = selText2.replace("$", "\$")

#die(print_r("[]", 1));
#console.log("[] " + $x)

if '.php' in winTitle:
    clipboard.fill_clipboard('echo "<pre>[' + label + '] ' + selText_php + '</pre>";')

if '.js' in winTitle or '.html' in winTitle:
    clipboard.fill_clipboard('console.log("[' + label + '] ' + selText_php + '");')

keyboard.send_keys("<ctrl>+v")

mapsedge_save.doSave(keyboard, time, window)
