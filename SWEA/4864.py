T = int(input())
for test_case in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()

    if str1 in str2:
        ans = 1
    else:
        ans = 0

    print(f"#{test_case} {ans}")
