T = int(input())

grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    scores = []

    for i in range(N):
        mid, fin, hw = map(int, input().split())
        total = mid * 0.35 + fin * 0.45 + hw * 0.2
        scores.append((total, i+1))   # (총점, 학생번호)

    # 총점 기준으로 내림차순 정렬
    scores.sort(reverse=True, key=lambda x: x[0])

    # K번 학생의 등수 찾기
    for idx in range(N):
        if scores[idx][1] == K:
            student_rank = idx
            break

    # 등수 기반 학점 계산
    per = N // 10   # 한 학점당 학생 수
    result = grade[student_rank // per]

    print(f"#{test_case} {result}")
