import sys

counter = system.exec_command("date '+%s'")
# counter = (int)counter - 1594923133
counter = int(counter) - 1594000000
six_digits_str = str(counter)[-7:] 

# Enter script code
time.sleep(.3)
#grab the abbreviation
keyboard.send_keys("<shift>+<ctrl>+<left>")

time.sleep(.3)
keyboard.send_keys("<ctrl>+x")
time.sleep(.2)
abbrev = clipboard.get_clipboard()
time.sleep(.2)

is_array = abbrev.startswith("a")

if is_array:
    flag = abbrev[4:]
else:
    flag = abbrev[3:]

#dialog.info_dialog(title='Window class', message=flag)

time.sleep(.1)

# delete the abbreviation
keyboard.send_keys("<backspace>")
time.sleep(.1)
#get the snippet   
keyboard.send_keys("<shift>+<home>")
time.sleep(.1)
#keyboard.send_keys("<shift>+<left>")
keyboard.send_keys("<ctrl>+x")
time.sleep(.2)
snip = clipboard.get_clipboard()
time.sleep(.1)

active_title = window.get_active_title()


if '.asp' in active_title:
    if is_array:
        tmp = 'call writeoutex("[{0}] {1}", 0)'.format(six_digits_str.strip(), snip.strip(), flag.strip()).strip()
        tmp = tmp + "\n"
        tmp = tmp + 'call writeoutex({1}, {2})'.format(six_digits_str.strip(), snip.strip(), flag.strip()).strip()
        clipboard.fill_clipboard(tmp)
    else:
        # Check if snip contains quotes
        if '"' in snip:
            # Replace only the first occurrence of quotes with doubled quotes
            snip_modified = snip.replace('"', '""')
        else:
            snip_modified = snip

        # Now use snip_modified in your format
        clipboard.fill_clipboard('call writeoutex("[{0}] {1}: " & {3}, {2}) \'--- test'.format(
            six_digits_str.strip(), snip_modified.strip(), flag.strip(), snip.strip()
        ))

if '.php' in active_title:
    clipboard.fill_clipboard('$s->writeout([\'[{0}] {1}: \' . print_r({1}, 1)], {2});'.format(six_digits_str.strip(), snip.strip(), flag.strip()))

if '.js' in active_title:
    clipboard.fill_clipboard('console.log("[{0}] {1}", {1});'.format(six_digits_str.strip(), snip.strip()).strip())

time.sleep(.2)
keyboard.send_keys("<ctrl>+v")

keyboard.send_keys("<ctrl>+s")
