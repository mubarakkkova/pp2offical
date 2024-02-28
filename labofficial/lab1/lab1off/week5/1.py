import re

def match_ab(text):
    pattern = "ab*"
    if re.match(pattern, text):
        return "Found a match"
    else:
        return "No match."


print(match_ab("ab"))
