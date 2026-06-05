_med = .2

def doSave(keyboard, time, window):
	keyboard.send_keys("<ctrl>+s")

def getLabel(time):
	secs = str(time.time())
	return secs[-8:]

def cutSelection(keyboard, time, clipboard):
	keyboard.send_keys("<end>")
	time.sleep(_med)
	keyboard.send_keys("<shift>+<home>")
	time.sleep(_med)
	keyboard.send_keys("<ctrl>+x")
	time.sleep(_med)
	selText = clipboard.get_clipboard()
	time.sleep(_med)
	return selText

def assign_and_paste(out2):
	clipboard.fill_clipboard(out2)
	time.sleep(.2)
	keyboard.send_keys("<ctrl>+v")