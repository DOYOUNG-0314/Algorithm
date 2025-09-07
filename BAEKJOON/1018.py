N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

result = float('inf')  # 최소값 저장

for i in range(N - 7):      # 시작 행
    for j in range(M - 7):  # 시작 열
        count_w = 0  # 좌상단이 W일 때 다시 칠해야 하는 칸
        count_b = 0  # 좌상단이 B일 때 다시 칠해야 하는 칸

        for x in range(8):
            for y in range(8):
                current = board[i + x][j + y]
                # (x+y) 짝수면 시작점과 같은 색, 홀수면 다른 색이어야 함
                if (x + y) % 2 == 0:
                    if current != 'W':  # W 시작일 때
                        count_w += 1
                    if current != 'B':  # B 시작일 때
                        count_b += 1
                else:
                    if current != 'B':  # W 시작일 때
                        count_w += 1
                    if current != 'W':  # B 시작일 때
                        count_b += 1

        result = min(result, count_w, count_b)

print(result)
