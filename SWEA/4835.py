T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_sum = -float('inf')
    min_sum = float('inf')

    for i in range(N - M + 1):
        window_sum = sum(nums[i:i+M])
        if window_sum > max_sum:
            max_sum = window_sum
        if window_sum < min_sum:
            min_sum = window_sum

    result = max_sum - min_sum
    print(f"#{tc} {result}")
