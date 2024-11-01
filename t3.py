def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
             stack.append(int(a / b))
             stack.append(int(token))
    return stack.pop()
