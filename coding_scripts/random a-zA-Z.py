# insert 12 character long string of random letters and numbers
# omits all vowels, K and Q, to avoid inadvertant profanity.
import string
import random
import re

res = "" . join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=50))

output = re.sub('([aeiouAEIOUkKqQ])*', '', res)


keyboard.send_keys(output[0:12])



