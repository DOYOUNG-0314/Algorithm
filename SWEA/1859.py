T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    
    max_future = 0
    profit = 0
    
    # 뒤에서 앞으로
    for price in reversed(prices):
        if price < max_future:
            profit += max_future - price
        else:
            max_future = price
    
    print(f"#{tc} {profit}")
