T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    # 무한대 경우
    if dist == 0 and r1 == r2:
        print(-1)
    # 교점 없음
    elif dist > r1 + r2 or dist < abs(r1 - r2):
        print(0)
    # 접하는 경우 (외접 또는 내접)
    elif dist == r1 + r2 or dist == abs(r1 - r2):
        print(1)
    # 교점 2개
    else:
        print(2)
