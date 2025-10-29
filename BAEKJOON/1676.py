N = int(input())
zeros = 0
i = 5

while i <= N:
    zeros += N // i
    i *= 5

print(zeros)
