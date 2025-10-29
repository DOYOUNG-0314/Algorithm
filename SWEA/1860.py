T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    ans = 1 
    if arr[0] < M:
        ans = 0
    else:
        for i in range(1, N // K):
            if arr[i * K] < (i + 1) * M:
                ans = 0
                break

    if ans == 0:
        print(f"#{test_case} Impossible")
    else:
        print(f"#{test_case} Possible")
