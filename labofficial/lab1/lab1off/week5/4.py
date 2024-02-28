import re

def upper_after_lower(text):
    pattern = r'(?:[A-Z]{1}[a-z])+'
    return re.findall(pattern, text)


print(upper_after_lower("IHFshdoUGisgdsjUGfushlo"))
