def reverse(board, x, y, color):
    N = len(board)
    board[x][y] = color
    opponent = 3 - color  # 1->2, 2->1
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1), (1,0), (1,1)]
    
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        tmp = []
        while 0<=nx<N and 0<=ny<N and board[nx][ny]==opponent:
            tmp.append((nx,ny))
            nx += dx
            ny += dy
        if 0<=nx<N and 0<=ny<N and board[nx][ny]==color:
            for tx, ty in tmp:
                board[tx][ty] = color

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    mid = N//2
    board[mid-1][mid-1] = 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1
    board[mid][mid] = 2

    for _ in range(M):
        y, x, color = map(int, input().split())
        reverse(board, x-1, y-1, color)

    black = sum(row.count(1) for row in board)
    white = sum(row.count(2) for row in board)
    print(black, white)
