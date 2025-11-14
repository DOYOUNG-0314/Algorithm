def dfs(v):
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            dfs(w)

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    
    # 인접리스트 초기화
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)  # 방향성 그래프

    S, G = map(int, input().split())
    visited = [0] * (V+1)

    dfs(S)

    ans = 1 if visited[G] else 0
    print(f"#{test_case} {ans}")
