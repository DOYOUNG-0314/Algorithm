T = int(input())

for _ in range(T):
    A, B, N = map(int, input().split())
    cnt = 0
    while A <= N and B <= N:
        if A < B:
            A += B
        else:
            B += A
        cnt += 1
    print(cnt)
