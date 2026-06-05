def doSave(keyboard, time, window):

	keyboard.send_keys("<ctrl>+s")

def cutSelection():
    keyboard.send_keys("<end>")
    time.sleep(_med)
    keyboard.send_keys("<shift>+<home>")
    time.sleep(_med)
    keyboard.send_keys("<ctrl>+x")
    time.sleep(_med)
    selText = clipboard.get_clipboard()
    time.sleep(_med)
    return selText

def getLabel():
    secs = str(time.time())
    return secs[-6:]
