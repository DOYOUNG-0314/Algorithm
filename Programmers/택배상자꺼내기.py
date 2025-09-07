def solution(n, w, num):
    # num의 행/열 계산
    row = (num - 1) // w
    k = (num - 1) % w
    col = k if row % 2 == 0 else w - 1 - k  # 0-based 왼쪽부터 열 인덱스

    last_row = (n - 1) // w
    answer = 0

    for r in range(row, last_row + 1):
        # r행에 실제 놓인 상자 개수(부분층 고려)
        if r < last_row:
            length = w
        else:
            rem = n - r * w
            length = rem if rem != 0 else w

        # r행이 짝수면 왼→오: [0 .. length-1]
        # r행이 홀수면 오→왼: [w-length .. w-1]
        if (r % 2 == 0 and col < length) or (r % 2 == 1 and col >= w - length):
            answer += 1

    return answer