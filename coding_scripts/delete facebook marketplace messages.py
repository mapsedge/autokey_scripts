# Author: 	Bill in KCMO
# Date:		2024-07-24

# adjust the x,y position for the hover icon ... on the first message
# you can use xev from the terminal to get the mouse position
# I use move_cursor + click_relative_self because I like to see the
# cursor land where I want it. You could also use mouse.click_absolute.

hovericon_x = 2285
hovericon_y = 258

count = 0
msgs_to_delete = 1
while (count < msgs_to_delete):
	count = count + 1
	# give the screen a chance to refresh after the last delete
	time.sleep(1)
	# go to the hover button and click
	mouse.move_cursor(2285, 258)
	time.sleep(.3)
	mouse.click_relative_self(0, 0, 1)
	time.sleep(.3)
	# navigate down to the "delete" item and select
  for i in "abc": # three letters = three iterations
  	keyboard.send_keys("<down>")
  	time.sleep(.1)
	time.sleep(.3)
	keyboard.send_keys("<enter>")
	# move to the confirm button and click
	mouse.move_cursor(3115, 646)
	time.sleep(.3)
	mouse.click_relative_self(0, 0, 1)
