T = int(input())

for test_case in range(1, T + 1):
    S = input().strip()
    cards = set()  # 중복 체크용
    suit_count = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
    error = False

    for i in range(0, len(S), 3):
        card = S[i:i+3]
        suit = card[0]
        num = card[1:]

        if card in cards:
            error = True
            break
        cards.add(card)
        suit_count[suit] += 1

    if error:
        print(f"#{test_case} ERROR")
    else:
        print(f"#{test_case} {13 - suit_count['S']} {13 - suit_count['D']} {13 - suit_count['H']} {13 - suit_count['C']}")
