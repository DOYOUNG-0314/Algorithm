def dfs(c, depth):
    global ans
    v[c] = 1

    if c == y:     # 목표 사람 도착 시
        ans = depth
        return

    for n in adj[c]:
        if not v[n]:
            dfs(n, depth + 1)


n = int(input())
x, y = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

v = [0] * (n + 1)
ans = -1    # 기본값 -1 (연결 안 될 경우)

dfs(x, 0)
print(ans)
