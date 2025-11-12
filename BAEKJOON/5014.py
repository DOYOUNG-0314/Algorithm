def bfs(s,e):
    q = []
    v = [0]*(F+1)
    q.append(s)
    v[s] = 1
    while q:
        c = q.pop(0)
        if c == e:
            return v[e] - 1
        for n in (c+U, c-D):
            if 1<=n<=F and v[n] == 0:
                q.append(n)
                v[n] = v[c]+1


    return 'use the stairs'

F, S, G, U, D = map(int, input().split())

ans = bfs(S,G)

print(ans)