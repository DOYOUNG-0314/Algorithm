def make_password(arr):
    i = 1
    while True:
        num = arr.pop(0) - i
        if num <= 0:
            arr.append(0)
            break
        arr.append(num)
        i += 1
        if i > 5:
            i = 1
    return arr

for _ in range(10):
    test_case = int(input())
    arr = list(map(int, input().split()))
    ans = make_password(arr)
    print(f"#{test_case}", *ans)
