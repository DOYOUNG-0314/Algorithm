# for test_case in range(1, 11):
#     M = int(input())
#     N = []
#     for i in range(100):
#         N[i] = int(input())
#         for j in range(M-1):
#             max(N) -= 1
#             min(N) += 1
#     result = max(N)-min(N)
#     print(f'#{test_case}'result)

    
for test_case in range(1, 11):
    M = int(input())  # 덤프 횟수
    N = list(map(int, input().split()))  # 한 줄에 100개 숫자 입력받기

    for _ in range(M):
        max_idx = N.index(max(N))
        min_idx = N.index(min(N))
        N[max_idx] -= 1
        N[min_idx] += 1

    result = max(N) - min(N)
    print(f'#{test_case} {result}')
