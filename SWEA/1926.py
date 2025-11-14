N = int(input())

for i in range(1, N+1):
    s = str(i)
    cnt = s.count('3') + s.count('6') + s.count('9')

    if cnt > 0:
        print('-' * cnt, end=" ")
    else:
        print(i, end=" ")
