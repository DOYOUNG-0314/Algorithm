def is_palindrome(s):
    return s == s[::-1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]
    answer = ""

    # 가로 검사
    for i in range(N):
        for j in range(N - M + 1):
            sub = board[i][j:j+M]
            if is_palindrome(sub):
                answer = sub
                break
        if answer:
            break

    # 세로 검사
    if not answer:
        for j in range(N):
            for i in range(N - M + 1):
                sub = "".join(board[i+k][j] for k in range(M))
                if is_palindrome(sub):
                    answer = sub
                    break
            if answer:
                break

    print(f"#{tc} {answer}")
