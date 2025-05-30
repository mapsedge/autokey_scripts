def getLabel():
    secs = str(int(time.time() * 1000000))  # Convert to microseconds and keep as integer
    return secs[-6:]

label = getLabel()
# label = label.replace('.', '0')
keyboard.send_keys(label)



