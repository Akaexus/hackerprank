seq = input().split()

# pretty crappy code
def xd(start, end):
    xd2(start, start, end)
    if start != end:
        xd(start+1, end)


def xd2(firstindex, start, end):
    if firstindex != start:
        global seq
        if int(seq[firstindex]) > int(seq[start]):
            seq[firstindex], seq[start] = seq[start], seq[firstindex]
    if start != end:
        xd2(firstindex, start+1, end)

xd(0, len(seq)-1)

print(' '.join(seq))