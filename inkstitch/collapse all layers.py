#Enter script code
#super + np_right6
time.sleep(1)
mouse.click_relative_self(0,0,1)

y = 25

for _ in range(5):
    
    #dialog.input_dialog("", str(y))
    #time.sleep(.2)
    time.sleep(.2)
    mouse.move_relative_self(0, y)
    time.sleep(.2)
    mouse.click_relative_self(0, 0, 1)

# dialog.info_dialog("", "done")
