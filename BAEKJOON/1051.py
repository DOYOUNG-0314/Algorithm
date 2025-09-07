N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

max_size = 1  # 최소 1칸은 정사각형임

for i in range(N):
    for j in range(M):
        # 가능한 최대 길이 = min(N-i, M-j)
        for size in range(1, min(N-i, M-j)):
            if board[i][j] == board[i+size][j] == board[i][j+size] == board[i+size][j+size]:
                max_size = max(max_size, size+1)

print(max_size * max_size)
