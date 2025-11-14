T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = max(arr) - min(arr)
    print(f"#{test_case} {ans}")