T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    # 첫 날짜의 연중 번호
    day1 = d1 + sum(days[1:m1])
    # 두 번째 날짜의 연중 번호
    day2 = d2 + sum(days[1:m2])
    # 첫 날짜를 1로 세므로 +1
    result = day2 - day1 + 1
    print(f"#{t} {result}")
