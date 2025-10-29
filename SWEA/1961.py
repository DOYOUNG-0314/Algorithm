T = int(input())

for t in range(1, T + 1):
    N = int(input())
    matrix = [list(input().split()) for _ in range(N)]
    
    # 90도 회전
    rotate_90 = [[matrix[N - j - 1][i] for j in range(N)] for i in range(N)]
    # 180도 회전
    rotate_180 = [[matrix[N - i - 1][N - j - 1] for j in range(N)] for i in range(N)]
    # 270도 회전
    rotate_270 = [[matrix[j][N - i - 1] for j in range(N)] for i in range(N)]

    print(f"#{t}")
    for i in range(N):
        print(
            ''.join(rotate_90[i]),
            ''.join(rotate_180[i]),
            ''.join(rotate_270[i])
        )
