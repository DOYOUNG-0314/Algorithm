T= int(input())
for test_case in range(1,T+1):
    N = int(input())
    v = [[0]*10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        a,b,c,d,col = map(int, input().split())
        for i in range(a,c+1):
            for j in range(b,d+1):
                if v[i][j] == 0:
                    v[i][j] = col
                elif v[i][j] != col and v[i][j] != 3:
                    cnt += 1
                    v[i][j] = 3
    print(f"#{test_case} {cnt}")
