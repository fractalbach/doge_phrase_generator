import random
import math

title = '''
______________________________________________________________________
                      The Doge Phrase Generator!
======================================================================
'''

mods = {"very", "so", "such", "much", "many", "quite"}

correctMods = {
    'noble': {'very', 'so', 'quite'},
    'fluffy': {'very', 'so', 'quite'},
    'thanks': {'much', 'many'}
}

words = {key for key in correctMods.keys()}

# ______________________________________________________________________
# Functions
# ----------------------------------------------------------------------

def pick1(S):
    return random.sample(S, 1)[0]


def generate():
    word = pick1(words)
    correct = correctMods[word]
    diff = mods - correct
    mod = pick1(diff)
    print(mod, word)

# ______________________________________________________________________    
# Main
# ----------------------------------------------------------------------

print(title)

for _ in range(0, 10):
    generate()
    
print()
