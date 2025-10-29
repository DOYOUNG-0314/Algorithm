n = int(input())

if n < 100:
    print(n)
else:
    count = 99
    for i in range(100, min(n, 999) + 1):
        a = i // 100
        b = (i // 10) % 10
        c = i % 10
        if a - b == b - c:
            count += 1
    print(count)
