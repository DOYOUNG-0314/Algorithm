n = input().strip()

count = [0] * 10

for ch in n:
    count[int(ch)] += 1

for i in range(10):
    print(i, end=" ")
print()

for i in range(10):
    print(count[i], end=" ")