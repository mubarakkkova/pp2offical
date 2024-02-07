from itertools import permutations

def permutation(word: str):
    return (''.join(x) for x in permutations(word))

print(list(permutation('12')))