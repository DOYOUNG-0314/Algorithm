import sys                     # 빠른 입력을 쓰기 위해 sys 모듈 사용
from collections import deque  # BFS용 큐(deque) 사용
input = sys.stdin.readline     # 표준 입력을 더 빠르게 읽기

dx = [0, 0, -1, 1]             # x 이동값: 상, 하, 좌, 우
dy = [-1, 1, 0, 0]             # y 이동값: 상, 하, 좌, 우

def bfs(x, y, field, visited, N, M):  # (x,y)에서 시작하는 BFS 함수
    q = deque()                        # 큐 생성
    q.append((x, y))                   # 시작 좌표 큐에 넣기
    visited[y][x] = True               # 시작 좌표 방문 표시

    while q:                           # 큐가 빌 때까지 반복
        cx, cy = q.popleft()           # 현재 좌표 꺼내기
        for i in range(4):             # 4방향 확인
            nx = cx + dx[i]            # 다음 x
            ny = cy + dy[i]            # 다음 y
            if 0 <= nx < M and 0 <= ny < N:                 # 범위 안이면
                if not visited[ny][nx] and field[ny][nx] == 1:  # 미방문이고 배추면
                    visited[ny][nx] = True                 # 방문 표시
                    q.append((nx, ny))                     # 큐에 추가

T = int(input())                    # 테스트 케이스 개수 입력

for _ in range(T):                  # 테스트 케이스만큼 반복
    M, N, K = map(int, input().split())  # 가로 M, 세로 N, 배추 수 K
    field = [[0] * M for _ in range(N)]  # N행 M열 밭(0으로 초기화)
    visited = [[False] * M for _ in range(N)]  # 방문 여부 배열

    for _ in range(K):              # 배추 좌표들 입력
        x, y = map(int, input().split())
        field[y][x] = 1             # 해당 위치에 배추 표시(1)

    count = 0                       # 지렁이(연결요소) 개수

    for y in range(N):              # 모든 칸 순회
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:   # 배추 있고 미방문이면
                bfs(x, y, field, visited, N, M)          # 그 덩어리 전부 탐색
                count += 1                                # 덩어리 하나 찾음 → +1

    print(count)                     # 해당 테스트 케이스의 정답 출력