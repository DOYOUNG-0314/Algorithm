L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())

# n이 집합 S에 있으면 좋은 구간 없음
if n in S:
    print(0)
else:
    # n보다 작은 최대값 L, n보다 큰 최소값 R 찾기
    left = 0
    right = 1001  # 문제 조건상 충분히 큰 값
    for x in S:
        if x < n:
            left = max(left, x)
        elif x > n:
            right = min(right, x)

    # 경우의 수 계산
    result = (n - left) * (right - n) - 1
    print(result)
