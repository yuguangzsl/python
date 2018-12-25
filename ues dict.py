vowels = ['a','e','i','o','u']
word   = input('provide a word to scarch for vowels:')
found  = {'a':0,'e':0,'i':0,'o':0,'u':0}

for k in word:
    if k in vowels:
        found[k] += 1

for m,n in sorted(found.items()) :
    if n!=0:
        print(m,'was','found',n,'times')
