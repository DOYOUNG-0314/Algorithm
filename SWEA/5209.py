def dfs(n, sm):
    global ans
    if sm >= ans:
        return

    if n == N:
        ans = min(ans,sm)

        return
    
    for j in range(0,N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm+lst[n][j])
            v[j] = 0



T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ans = float('inf')
    v = [0]*N
    dfs(0, 0)
    print(f"#{test_case} {ans}")