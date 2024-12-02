
def isValid(data):
    stack = []
    match = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    for i in range(len(data)):
        if data[i] in match:
            stack.append(data[i])
        elif len(data) == 0 or len(stack) == 0 or data[i] != match[stack.pop()]:
            return False
    return len(stack) == 0


print(isValid ("]") )