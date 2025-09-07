T = int(input())

for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    
    total_m = m1 + m2
    extra_h = total_m // 60  # 60분 이상이면 시로 올림
    total_m = total_m % 60   # 남은 분
    
    total_h = h1 + h2 + extra_h
    total_h = total_h % 12
    if total_h == 0:
        total_h = 12  # 12시간제 처리
    
    print(f"#{tc} {total_h} {total_m}")
