T = int(input())
for _ in range(T):
    tc = int(input())  # 테스트 케이스 번호
    scores = list(map(int, input().split()))

    freq = [0] * 101  # 점수 0~100
    for s in scores:
        freq[s] += 1

    max_freq = max(freq)
    # 최빈수 중 가장 큰 점수 찾기
    for i in range(100, -1, -1):
        if freq[i] == max_freq:
            mode = i
            break

    print(f"#{tc} {mode}")
