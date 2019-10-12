seq = input().lower()
sequences = []
currentSequence = ''

for letter in seq:
    if len(currentSequence):
        if letter == currentSequence[0]:
            currentSequence += letter
        else:
            sequences.append(currentSequence)
            currentSequence = ''
    else:
        currentSequence += letter
sequences.append(currentSequence)
if (len(seq)):
    print(max(sequences, key = len)[0])