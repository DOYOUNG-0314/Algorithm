T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 크기 N, 파리채 크기 M
    board = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열 입력

    max_kill = 0  # 최대 파리 수 저장

    # M x M 영역을 시작할 수 있는 좌표는 (0 ~ N-M)까지 가능
    for i in range(N - M + 1):  
        for j in range(N - M + 1):
            total = 0
            # (i, j)에서 시작하는 M x M 영역의 파리 수 합산
            for x in range(i, i + M):
                for y in range(j, j + M):
                    total += board[x][y]

            # 최댓값 갱신
            max_kill = max(max_kill, total)

    print(f"#{t} {max_kill}")