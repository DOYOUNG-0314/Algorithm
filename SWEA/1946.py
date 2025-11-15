T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = ""

    for _ in range(N):
        c, v = input().split()
        result += c * int(v)

    print(f"#{test_case}")
    # 10 문자씩 끊어서 출력
    for i in range(0, len(result), 10):
        print(result[i:i+10])
