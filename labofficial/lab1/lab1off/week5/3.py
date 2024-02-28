import re

def lowercase_underline_sequence(text):
    pattern = r'[a-z]{1}(?:_[a-z]{1})+'
    return re.findall(pattern, text)


input_string = "ok_i_finished_lab5 and i go to sleep"
print(lowercase_underline_sequence(input_string))
