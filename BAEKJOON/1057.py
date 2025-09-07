N, jimin, hansu = map(int, input().split())

round = 0
while jimin != hansu:
    jimin = (jimin + 1) // 2
    hansu = (hansu + 1) // 2
    round += 1

print(round)
