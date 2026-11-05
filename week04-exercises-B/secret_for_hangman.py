import random

words = ['programming', 'polymorphism', 'optimization', 'inheritance', 'encapsulation',
         'composition', 'debugging', 'compiler']

r = random.randint(0, len(words)-1)

word = words[r]

print(word)

secret = ""

secret += word[0]
for i in range(1, len(word)-1):
    secret += '_'
secret += word[-1]

print(secret)

