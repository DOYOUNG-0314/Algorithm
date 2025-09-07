T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    N = int(input())
    res = []

    for m in money:
        cnt = N // m      # 해당 단위 개수
        res.append(cnt)
        N = N % m         # 나머지로 다음 단위 계산

    print(f"#{tc}")
    print(' '.join(map(str, res)))
