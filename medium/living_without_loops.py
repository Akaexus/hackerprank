string = input()
counter = 0

# pretty crappy code
def xd(start, end):
    xd2(start, start, end)
    if start != end:
        xd(start+1, end)


def xd2(firstindex, start, end):
    if firstindex != start:
        a = string[firstindex:start]
        if a[0] == a[-1]:
            global counter
            counter += 1
    if start != end:
        xd2(firstindex, start+1, end)

xd(0, len(string))
print(counter)