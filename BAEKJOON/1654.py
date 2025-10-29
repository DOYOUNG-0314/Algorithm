K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

left, right = 1, max(lines)
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(line // mid for line in lines)
    
    if count >= N:
        answer = mid  # 가능한 길이
        left = mid + 1
    else:
        right = mid - 1

print(answer)
