T = int(input())

for test_case in range(1, T+1):
    s = input().strip()
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()  # 같은 문자면 제거
        else:
            stack.append(ch)

    print(f"#{test_case} {len(stack)}")
