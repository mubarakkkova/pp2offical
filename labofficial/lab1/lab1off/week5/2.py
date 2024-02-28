import re

def match_a23b(text):
    pattern = "ab{2,3}"
    if re.match(pattern, text):
        return "Found a match"
    else:
        return "No match."


print(match_a23b("abb"))