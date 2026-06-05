# Enter script code


out = """(function($){
    $(document).ready(function(){
        
    });
})(jQuery);"""

keyboard.send_keys(out)
keyboard.send_key("<down>")
i = 1
while i < 6:
    keyboard.send_keys("<shift>+<up>")
    i += 1
    
keyboard.send_keys("<shift>+<home>")
    
i = 1
while i < 20:
    keyboard.send_keys("<shift>+<tab>")
    i += 1
    
keyboard.send_key("<down>")
keyboard.send_key("<backspace>")
keyboard.send_key("<backspace>")
keyboard.send_key("<up>")
keyboard.send_key("<up>")
keyboard.send_key("<tab>")

keyboard.send_key("<up>")
keyboard.send_key("<up>")
keyboard.send_key("<home>")
keyboard.send_key("<tab>")

keyboard.send_key("<down>")
keyboard.send_key("<tab>")
keyboard.send_key("<tab>")