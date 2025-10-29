T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    dx = [1, 0, 1, 1]
    dy = [0, 1, 1, -1]

    found = False

    for y in range(N):
        for x in range(N):
            if board[y][x] == 'o':
                for dir in range(4):
                    cnt = 1
                    nx, ny = x, y
                    for _ in range(4):
                        nx += dx[dir]
                        ny += dy[dir]
                        if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt >= 5:
                        found = True
                        break
            if found:
                break
        if found:
            break

    print(f"#{test_case} {'YES' if found else 'NO'}")
