import re
import time

time.sleep(0.2)  # delayto get fingers off the keys
# Send Ctrl+X to cut selected text
keyboard.send_keys("<ctrl>+x")
time.sleep(0.2)  # wait for clipboard to update

# Get the selected text from clipboard
text = clipboard.get_clipboard()

# Replacement functions
def replace_request(match):
    key = match.group(1).strip()
    return f"#req.{key.lower()}#"

def replace_rs(match):
    prefix = match.group(1).strip()
    key = match.group(2).strip()
    return f"#{prefix}.{key.lower()}#"

# Compile patterns with flexible spacing
request_pattern = re.compile(r'<%\s*=\s*request\s*\(\s*"([^"]+)"\s*\)\s*%>')
rs_pattern = re.compile(r'<%\s*=\s*(rs\d*)\s*\(\s*"([^"]+)"\s*\)\s*%>')

# Initialize a variable to track changes
previous_text = ""
while True:
    # Store current text for comparison
    current_text = text

    # Perform substitutions
    text = request_pattern.sub(replace_request, text)
    text = rs_pattern.sub(replace_rs, text)

    # Check if any replacements were made
    if text == current_text:
        break  # No change, exit loop

# Fallback to simpler patterns if no more "#req." or "#rs" found
if "#req." not in text and "#rs" not in text:
    # Compile fallback patterns
    request_pattern_fallback = re.compile(r'request\s*\(\s*"([^"]+)"\s*\)')
    rs_pattern_fallback = re.compile(r'(rs\d*)\s*\(\s*"([^"]+)"\s*\)')
    
    # Loop until no more replacements
    while True:
        current_text = text
        text = request_pattern_fallback.sub(replace_request, text)
        text = rs_pattern_fallback.sub(replace_rs, text)
        if text == current_text:
            break

# Set processed text back to clipboard
clipboard.fill_clipboard(text)

# Paste back if desired
keyboard.send_keys("<ctrl>+v")