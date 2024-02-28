import re

def insert_spaces(text):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1 \2', text)


print(insert_spaces('helloWorld'))

