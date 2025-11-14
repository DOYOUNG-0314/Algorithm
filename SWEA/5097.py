T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = arr[M%N]
    print(f"#{test_case} {ans}")
