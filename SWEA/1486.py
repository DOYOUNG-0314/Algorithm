def dfs(n, sm):
    global ans
    if n == N:
        if B <= sm:
            ans = min(ans,sm-B)

        return
    dfs(n+1, sm+arr[n])
    dfs(n+1,sm)


T = int(input())
for test_case in range(1,T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = N*10000
    dfs(0, 0)

    print(f"#{test_case} {ans}")
