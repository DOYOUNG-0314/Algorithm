N = int(input())
friends = [input().strip() for _ in range(N)]

max_count = 0
for i in range(N):
    two_friends = set()
    for j in range(N):
        if friends[i][j] == 'Y':  # i와 j는 직접 친구
            two_friends.add(j)
            for k in range(N):
                if friends[j][k] == 'Y':  # j와 k도 친구라면
                    two_friends.add(k)
    if i in two_friends:
        two_friends.remove(i)  # 자기 자신 제거
    max_count = max(max_count, len(two_friends))

print(max_count)
