from collections import deque

def bfs(si, sj):
    q = deque()
    v = [[0]*N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        if arr[ci][cj] == 3:
            return v[ci][cj] - 2  # 출발-도착 제외

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

    return 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j

    ans = bfs(si, sj)
    print(f"#{test_case} {ans}")
