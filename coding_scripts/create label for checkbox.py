import re

time.sleep(1)
keyboard.send_keys("<ctrl>+x")
time.sleep(.2)
template_html = clipboard.get_clipboard()
time.sleep(.2)

# Extract the name attribute
match_name = re.search(r'name=["\']([^"\']+)["\']', template_html)
name_attr = match_name.group(1) if match_name else ''

# Check if id attribute exists
match_id = re.search(r'id=["\']([^"\']*)["\']', template_html)
if match_id:
    id_attr = match_id.group(1)
else:
    # If no id, set id = name
    id_attr = name_attr
    # Add id attribute to the input HTML
    # Insert id after the name attribute
    def add_id(match):
        return match.group(0) + ' id="' + id_attr + '"'
    template_html = re.sub(r'(name=["\'][^"\']+["\'])', add_id, template_html, count=1)

# Create the label HTML
label_html = f'<label for="{id_attr}">{id_attr}</label>'

# Combine label and input
# Ensure label comes before input
keyboard.send_keys(label_html)
keyboard.send_keys(template_html)

