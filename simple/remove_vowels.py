sentence = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

print(''.join(list(filter(lambda l: l.lower() not in vowels, sentence))))