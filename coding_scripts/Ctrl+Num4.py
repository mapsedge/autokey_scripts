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

def main():
    winTitle = window.get_active_title()
    label = getLabel()

    selText = cutSelection()
    selText_asp = selText.replace('"', '""')
    selText2 = selText.replace("\"", "\\\"")
    selText_php = selText2.replace("$", "\$")

    if '.php' in winTitle:
        clipboard.fill_clipboard('die("<pre>[' + label + '] ' + selText_php + ': " . print_r(' + selText + ', 1) . "</pre>");')


    if '.asp' in winTitle:
        clipboard.fill_clipboard('call writeout("[' + str(label) + '] ' + selText_asp + ': ' + selText_asp + '", 2)')
        

    if '.js' in winTitle or '.html' in winTitle:
        clipboard.fill_clipboard('console.log("[' + label + '] ' + selText_php + '", ' + selText + ');')
        
    keyboard.send_keys('<ctrl>+v')
    mapsedge_save.doSave(keyboard, time, window)
    exit

main()
