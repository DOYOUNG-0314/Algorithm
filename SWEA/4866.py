T = int(input())
for tc in range(1, T + 1):
    line = input().strip()
    stack = []
    ok = 1

    for ch in line:
        if ch in "{(":
            stack.append(ch)
        elif ch == "}":
            if not stack or stack[-1] != "{":
                ok = 0
                break
            stack.pop()
        elif ch == ")":
            if not stack or stack[-1] != "(":
                ok = 0
                break
            stack.pop()
        # 다른 문자는 무시

    if stack:
        ok = 0

    print(f"#{tc} {ok}")
