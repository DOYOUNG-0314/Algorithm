def calc(tokens):
    stack = []
    ops = ['+', '-', '*', '/']

    for t in tokens:
        if t.isdigit():  # 숫자면 push
            stack.append(int(t))
        elif t in ops:
            if len(stack) < 2:
                return "error"
            b = stack.pop()
            a = stack.pop()

            if t == '+':
                stack.append(a+b)
            elif t == '-':
                stack.append(a-b)
            elif t == '*':
                stack.append(a*b)
            elif t == '/':
                stack.append(a//b)
        elif t == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return "error"
        else:
            return "error"

    return "error"  # . 못만났을 경우


T = int(input())
for tc in range(1, T+1):
    tokens = input().split()
    print(f"#{tc} {calc(tokens)}")
