#Enter script code
def getLabel():
    secs = str(time.time())
    return secs[-6:]

def main():
    label = getLabel()
    
    clipboard.fill_clipboard('console.log("[' + label + ']", new Date().toString("yyyy-MM-dd HH:mm"));')
    time.sleep(.5)
    keyboard.send_keys("<ctrl>+v")
    
main()