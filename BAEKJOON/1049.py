N, M = map(int, input().split())
min_package = 1001
min_single = 1001

for _ in range(M):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

# 세 가지 경우 계산
cost1 = ((N // 6) + 1) * min_package   # 패키지로만
cost2 = N * min_single                 # 낱개로만
cost3 = (N // 6) * min_package + (N % 6) * min_single  # 혼합

print(min(cost1, cost2, cost3))
