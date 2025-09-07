for t in range(1, 11):  # 총 10개 테스트케이스
    N = int(input())  # 건물 개수
    heights = list(map(int, input().split()))  # 건물 높이 리스트

    view_count = 0  # 조망권 확보된 세대 수

    for i in range(2, N - 2):  # 양쪽 2칸은 건물 없음
        # 양쪽 2칸에서 가장 높은 건물 찾기
        max_side = max(heights[i - 2], heights[i - 1],
                       heights[i + 1], heights[i + 2])

        if heights[i] > max_side:  # 조망권 확보됨
            view_count += heights[i] - max_side

    print(f"#{t} {view_count}")
