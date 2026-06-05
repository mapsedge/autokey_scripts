# Enter script code
import sys
counter = system.exec_command("date '+%s'")
counter = int(counter) - 1594000000
six_digits_str = str(counter)[-7:] 

time.sleep(.1)
active_title = window.get_active_title()
time.sleep(.1)

if '.asp' in active_title:
        
    clipboard.fill_clipboard("call writeoutex (\"[" + str(six_digits_str) + "] \" & now, 2)")
    time.sleep(.2)
    keyboard.send_keys("<ctrl>+v") 
    
if '.php' in active_title:
    keyboard.send_keys('$s->writeout(date("Y/m/d H:i:s"), 2);')

if '.js' in active_title:
    keyboard.send_keys('let testDate = new Date(); console.log("' + six_digits_str + '", testDate);')

time.sleep(.2)
keyboard.send_keys("<ctrl>+s") 