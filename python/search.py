def search(word:str) -> set:
    """Return any vowels found in a supplied word"""
    vowels = set('aeiou')
   # woed = input('provide a word to search for vowels:')
    found = vowels.intersection(set(word)) 
#    for vowel in found :
 #       print(vowel)
    return bool(word)
