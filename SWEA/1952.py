def dfs(n, sm):
    global ans
    if sm >= ans:
        return
    if n >= 13:
        ans = min(ans, sm)
        return
    dfs(n + 1, sm + day * lst[n])  # 1일 이용권
    dfs(n + 1, sm + mon)            # 1달 이용권
    dfs(n + 3, sm + mon3)           # 3달 이용권
    dfs(n + 12, sm + year)          # 1년 이용권


T = int(input())

for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    ans = float('inf')
    dfs(1, 0)
    print(f"#{test_case} {ans}")
