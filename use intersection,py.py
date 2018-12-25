vowels = set('aeiou')
word   = input('provide a word to serch for vowels:')
u = set(word).intersection(vowels)
for i in u:
    print(i)
