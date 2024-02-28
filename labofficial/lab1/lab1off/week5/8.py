import re

def split_to_uppercase(text):
    pattern = r'[a-z]'
    return re.sub(pattern, lambda x: x.group().upper(), text)


print(split_to_uppercase("okayyy"))
