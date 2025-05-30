#Enter script code
x = """(function($){
	
})(jQuery);
"""

clipboard.fill_clipboard(x)
time.sleep(.2)
keyboard.send_keys("<ctrl>+v")
time.sleep(.2)
keyboard.send_keys("<up><up><home><home>")
time.sleep(.2)
keyboard.send_keys("<escape>")
time.sleep(.2)
keyboard.send_keys("<tab>")
