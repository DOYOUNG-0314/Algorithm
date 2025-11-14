T = int(input())
dp = [0]*31
dp[0] = 0
dp[1] = 1
dp[2] = 3
for i in range(3, 31):
    dp[i] = dp[i-1] + 2*dp[i-2]

for test_case in range(1, T+1):
    N = int(input())
    print(f"#{test_case} {dp[N//10]}")
