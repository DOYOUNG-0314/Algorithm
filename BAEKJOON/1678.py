from collections import deque

T, M, N = map(int, input().split())
trains = []

for _ in range(T):
    data = input().split()
    name = data[0]
    time = int(data[1])
    trains.append((name, time))

current_time = M
last_train = None

for _ in range(N):
    # 각 기차 도착 시간 계산
    wait = [(name, (time - current_time + 60) % 60) for name, time in trains]
    # 가장 빨리 오는 기차 선택
    wait.sort(key=lambda x: x[1])
    last_train = wait[0][0]
    # 도착 시각 갱신
    current_time += wait[0][1]

print(last_train)
