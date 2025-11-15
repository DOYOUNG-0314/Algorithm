T = int(input())

for test_case in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    # 시와 분 합산
    h = h1 + h2
    m = m1 + m2

    # 분이 60 이상이면 시로 올리기
    if m >= 60:
        h += m // 60
        m = m % 60

    # 12시간제 처리 (1~12)
    h = h % 12
    if h == 0:
        h = 12

    # 출력
    print(f"#{test_case} {h} {m}")
