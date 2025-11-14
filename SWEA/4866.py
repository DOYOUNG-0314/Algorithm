T = int(input())
for test_case in range(1,T+1):
    c = input()
    stack=[]
    ans = 0
    for ch in c:
        if ch =='(' or ch == '{':
            stack.append(ch)
        elif ch ==')':
            if stack and stack[-1] == '(':
                ans = 1
                stack.pop(-1)
            else:
                ans = 0
                break 
        elif ch =='}':
            if stack and stack[-1] == '{':
                ans = 1
                stack.pop(-1)
            else:
                ans = 0
                break
    if stack :
        ans = 0
    print(f"#{test_case} {ans}")        