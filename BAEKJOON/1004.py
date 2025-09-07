import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        
        # 출발점 원 내부 여부
        start_in = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2
        # 도착점 원 내부 여부
        end_in = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2
        
        # 포함 여부가 다르면 진입/이탈 필요
        if start_in != end_in:
            count += 1

    print(count)