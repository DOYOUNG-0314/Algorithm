# 체스 좌표 변환
def pos_to_xy(pos):
    col = ord(pos[0]) - ord('A')
    row = int(pos[1]) - 1
    return col, row

def xy_to_pos(x, y):
    return chr(x + ord('A')) + str(y + 1)

# 이동 방향 매핑
moves = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1),
}

king, stone, N = input().split()
N = int(N)
kx, ky = pos_to_xy(king)
sx, sy = pos_to_xy(stone)

for _ in range(N):
    cmd = input().strip()
    dx, dy = moves[cmd]

    nkx, nky = kx + dx, ky + dy

    # 킹이 보드 밖으로 나가면 무시
    if not (0 <= nkx < 8 and 0 <= nky < 8):
        continue

    # 킹이 돌과 겹치면
    if nkx == sx and nky == sy:
        nsx, nsy = sx + dx, sy + dy
        # 돌도 보드 안이어야 함
        if not (0 <= nsx < 8 and 0 <= nsy < 8):
            continue
        # 돌 이동
        sx, sy = nsx, nsy

    # 킹 이동
    kx, ky = nkx, nky

print(xy_to_pos(kx, ky))
print(xy_to_pos(sx, sy))
