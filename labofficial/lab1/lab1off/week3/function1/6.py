def reverser(word):
    word = word.split()
    word.reverse()
    return word
h = "hello amazing world"
print(reverser(h))