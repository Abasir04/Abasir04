# encode 1
words = list(input("enter a sentence: "))
keys = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5, ' ': ' '}
for word in words:
    for letter in word:
        if letter in 'aeiou ':
            letter = keys[letter]
        else:
            letter = letter + 'a'
        print(letter, end='')

# encode 2
sentence = input("Enter a word you wish to encode: ")
words = sentence.split(' ')
keys = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
for word in words:
    for letter in word:
        if letter in 'aeiou':
            letter = keys[letter]
        else:
            letter = letter + 'a'
        print(letter, end='')
