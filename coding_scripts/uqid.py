time.sleep(.25)
output = system.exec_command("date '+%s'")
keyboard.send_keys(output)