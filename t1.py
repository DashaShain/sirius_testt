d = input()
d = d.split(' ')
stack = []
for i in d:
    if i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a-b)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(a // b)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    else:
        stack.append(int(i))
print(stack[0])
