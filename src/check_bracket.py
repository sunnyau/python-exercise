

def validate(string):
    # return True
    stack = []
    for c in string:
        if c == '{' or c == '(':
            stack.append(c)
        elif c == '}':
            if len(stack) == 0:
                return False
            elif stack[-1] == '{':
                stack.pop()   
        elif c == ')':
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
    return len(stack) == 0
