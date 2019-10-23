def checkBracketing(string):
    brackets = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    stack = []
    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if len(stack) and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(checkBracketing(input()))