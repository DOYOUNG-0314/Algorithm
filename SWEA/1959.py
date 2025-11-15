T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 작은 배열을 슬라이드
    if N > M:
        A, B = B, A
        N, M = M, N

    arr = []

    for i in range(M - N + 1):
        cnt = 0
        for j in range(N):
            cnt += A[j] * B[i + j]
        arr.append(cnt)

    ans = max(arr)
    print(f"#{test_case} {ans}")
