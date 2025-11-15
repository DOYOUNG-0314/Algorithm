def lee(left, right, target, cnt):
    mid = int((left+right)/2)
    cnt += 1
    if target < mid:
        right = mid
        return lee(left, right, target, cnt)
    elif target > mid:
        left = mid
        return lee(left, right, target, cnt)
    else:
        return cnt

T = int(input())
for test_case in range(1,T+1):
    P, Pa, Pb = map(int, input().split())
    if lee(1,P,Pa,0) < lee(1,P,Pb,0):
        ans = 'A'
    elif lee(1,P,Pa,0) > lee(1,P,Pb,0):
        ans = 'B'
    else:
        ans = 0
    print(f"#{test_case} {ans}") 