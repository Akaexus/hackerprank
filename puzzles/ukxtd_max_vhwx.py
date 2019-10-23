def caesarCrypt(string, offset):
    offset = offset % 26
    # offset = 26 - offset
    # lower letters 97 - 122
    # upper letters 65 - 90
    newString = ''
    for letter in [ord(l) for l in list(string)]:
        uppercase = letter in range(65, 90+1)
        letter += offset
        if uppercase and letter not in range(65, 90 + 1):
            letter = (letter - 65) % 26 + 65
        if not uppercase and letter not in range(97, 122 + 1):
            letter = (letter - 97) % 26 + 97
        newString += chr(letter)
    return newString


print(' '.join(map(lambda s: caesarCrypt(s, 7), input().split())))

