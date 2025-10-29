import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:
    lo, hi = 1, 10**9
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        newZ = ((Y + mid) * 100) // (X + mid)
        if newZ > Z:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)
