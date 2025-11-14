def bfs(si,sj):
    q = []
    v = [[0]*N for _ in range(N)]
    q.append((si,sj))
    v[si][sj]=1

    while q:
        c = q.pop(0)
        ci = c[0]
        cj = c[1]
        if arr[ci][cj] == 3:
            return 1
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni = ci+di
            nj = cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                v[ni][nj] = 1
                q.append((ni,nj))
        
    return 0

T =int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j
    ans = bfs(si,sj)
    print(f"#{test_case} {ans}")
