#Enter script code
import string
import random
import re

res = "" . join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=50))

output = re.sub('([aeiouAEIOUkKqQ])*', '', res)


keyboard.send_keys(output[0:12])



