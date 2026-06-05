winClass = window.get_active_class()
if "dolphin.dolphin" in winClass:
    keyboard.send_key("<menu>")
    keyboard.send_key("c")
    keyboard.send_key("e")