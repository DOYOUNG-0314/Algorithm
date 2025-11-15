T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    seen_digits = set()
    k = 0

    while len(seen_digits) < 10:
        k += 1
        num = N * k
        seen_digits.update(str(num))  # 각 자리수를 set에 추가

    print(f"#{test_case} {num}")
