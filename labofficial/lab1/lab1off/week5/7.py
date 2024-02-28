import re

def replace_snakecase_on_camelcase(text):
    pattern = r'_([a-z])'
    return re.sub(pattern, lambda x: x.group(1).upper(), text)


print(replace_snakecase_on_camelcase('hello_world'))