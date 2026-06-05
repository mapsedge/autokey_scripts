# Enter script code
active_title = window.get_active_title()

if '.asp' in active_title:
    keyboard.send_keys("'---------------------------------------------------------------------------------<enter>")
    exit
    
if '.php' in active_title:
    keyboard.send_keys('//--------------------------------------------------------------------------------<enter>')
    exit

if '.js' in active_title:
    keyboard.send_keys('//--------------------------------------------------------------------------------<enter>')
    exit
 