# insert a random number of -length- digits.

length = 6

def getLabel():
    secs = str(int(time.time() * 1000000))  # Convert to microseconds and keep as integer
    return secs[-length:]

label = getLabel()
# label = label.replace('.', '0')
keyboard.send_keys(label)



