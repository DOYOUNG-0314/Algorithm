T = int(input())
for tc in range(1, T+1):
    # 입력: 9x9 정수 그리드
    grid = [list(map(int, input().split())) for _ in range(9)]

    valid = True

    # 1) 행 검사: 각 행에 중복이 있으면 invalid
    for r in range(9):
        if len(set(grid[r])) != 9:
            valid = False
            break

    # 2) 열 검사: 각 열에 중복이 있으면 invalid
    if valid:
        for c in range(9):
            col = [grid[r][c] for r in range(9)]
            if len(set(col)) != 9:
                valid = False
                break

    # 3) 3x3 블록 검사: 각 블록에 중복이 있으면 invalid
    if valid:
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                block = []
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        block.append(grid[r][c])
                if len(set(block)) != 9:
                    valid = False
                    break
            if not valid:
                break

    print(f"#{tc} {1 if valid else 0}")
