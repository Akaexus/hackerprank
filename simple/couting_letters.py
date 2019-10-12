sentence = list(filter(lambda l: l.isalpha(), input().lower()))
if len(sentence):
    counters = {}
    for letter in sentence:
        if letter not in counters:
            counters[letter] = 1
        else:
            counters[letter] += 1
    mostOccurences = max(counters.values())
    mostOccured = list(filter(lambda c: counters[c] == mostOccurences, counters))

    print(sorted(mostOccured)[0])

