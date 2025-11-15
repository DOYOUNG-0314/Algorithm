T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    distance = 0
    speed = 0
    for _ in range(N):
        c, s = map(int,input().split())
        if c == 0:
            pass  # 속도 그대로
        elif c == 1:
            speed += s
        else:  # 감속
            speed -= s
            if speed < 0:
                speed = 0
        distance += speed 
    print(f"#{test_case} {distance}")
