for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

  # 1. 각 행의 합
    for row in arr:
        max_sum = max(max_sum, sum(row))

    # 2. 각 열의 합
    for j in range(100):
        col_sum = sum(arr[i][j] for i in range(100))
        max_sum = max(max_sum, col_sum)

    # 3. 왼쪽 위 → 오른쪽 아래 대각선
    diag1 = sum(arr[i][i] for i in range(100))
    max_sum = max(max_sum, diag1)

    # 4. 오른쪽 위 → 왼쪽 아래 대각선
    diag2 = sum(arr[i][99 - i] for i in range(100))
    max_sum = max(max_sum, diag2)

    print(f'#{test_case} {max_sum}') 