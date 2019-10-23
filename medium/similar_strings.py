a = input()
b = input()

def similar(a, b):
    if len(a)-1 != len(b):
        return False
    offset = 0
    for bindex in range(len(b)):
        if a[bindex + offset] != b[bindex]:
            if offset == 0:
                offset += 1
            else:
                return False
    return True

print('TAK' if similar(a, b) else 'NIE')
