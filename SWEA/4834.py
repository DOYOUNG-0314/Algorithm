T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = input().strip()  # 숫자가 붙어서 들어옴

    count = {str(i):0 for i in range(10)}

    for ch in cards:
        count[ch] += 1

    # 최대 개수 찾기, 같으면 숫자가 큰 쪽
    max_count = -1
    max_num = -1
    for num in range(10):
        num_str = str(num)
        if count[num_str] > max_count or (count[num_str] == max_count and num > max_num):
            max_count = count[num_str]
            max_num = num

    print(f"#{test_case} {max_num} {max_count}")
