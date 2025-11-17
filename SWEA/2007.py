T = int(input())

for test_case in range(1, T+1):
    s = input().strip()
    ans = 0

    for l in range(1, 11):
        pattern = s[:l]
        # 다음 위치에서 패턴과 같은지 확인
        if s[l:2*l] == pattern:
            ans = l
            break

    print(f"#{test_case} {ans}")
