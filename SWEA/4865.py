T = int(input())
for test_case in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()

    count_dict = {}

    # str1에 있는 문자만 기준으로 dictionary 생성
    for ch in str1:
        count_dict[ch] = count_dict.get(ch, 0)

    # str2에서 str1 문자 등장 횟수 세기
    for ch in str2:
        if ch in count_dict:
            count_dict[ch] += 1

    # 가장 많이 나온 문자 개수 찾기
    ans = max(count_dict.values())

    print(f"#{test_case} {ans}")
