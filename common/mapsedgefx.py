def load_api(api_keyboard, api_mouse, api_store, api_system, api_window, api_clipboard, api_highlevel, api_dialog, api_engine):
    global keyboard, mouse, store, system, window, clipboard, highlevel, dialog, engine  # Define the API class instances as globals
    # then put the given instances into the script globals
    keyboard = api_keyboard
    mouse = api_mouse
    store = api_store
    system = api_system
    window = api_window
    clipboard = api_clipboard
    highlevel = api_highlevel
    dialog = api_dialog
    engine = api_engine

def getText():
    keyboard.send_keys("<end>")
    time.sleep(.1)
    keyboard.send_keys("<shift>+<home>")
    time.sleep(.1)
    keyboard.send_keys("<ctrl>+<x>")

def getLabel():
    secs = time.time()
    return secs[-6:]

def paste():
    keyboard.send_keys("<ctrl>+y")
