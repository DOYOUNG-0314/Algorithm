T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    arr = [abs(c) for c in a]  

    b = min(arr)           
    ans = arr.count(b)         

    print(f"#{test_case} {b} {ans}")
