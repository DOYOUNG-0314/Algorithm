def dfs(n, sm, cnt):
    global ans
    if n == N:
        if sm == K and cnt == CNT:
            ans += 1
        return

    # n번째 원소를 포함하는 경우
    dfs(n + 1, sm + lst[n], cnt + 1)
    # n번째 원소를 포함하지 않는 경우
    dfs(n + 1, sm, cnt)

T = int(input())
for test_case in range(1, T + 1):
    CNT, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = 12
    ans = 0

    dfs(0, 0, 0)

    print(f'#{test_case} {ans}')
