def fight(a ,b):
    if arr[a]==arr[b]:
        return a
    elif arr[a]==1 and arr[b]==2:
        return b
    elif arr[a]==1 and arr[b]==3:
        return a
    elif arr[a]==2 and arr[b]==3:
        return b
    elif arr[a]==2 and arr[b]==1:
        return a
    elif arr[a]==3 and arr[b]==1:
        return b
    else:
        return a

def tournament(arr, start, end):
    if start == end:
        return start
    mid = (start+end)//2
    left = tournament(arr, start, mid)
    right = tournament(arr, mid+1, end)
    return fight(left,right)



T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = tournament(arr, 0, N-1)
    print(f"#{test_case} {ans+1}")
    