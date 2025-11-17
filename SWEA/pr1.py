T = int(input())
for test_case in range(1,T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = 0
    m = 0
    if m1 + m2 >= 60:
        m = (m1 + m2)-60
        h += 1
    else: 
        m = m1+m2
    
    if h+(h1+h2) >24:
        h = h+(h1+h2)-24
    elif h+(h1+h2) > 12:
        h = h+(h1+h2)-12
    else:
        h = h+(h1+h2) 
       
    print(f"#{test_case} {h} {m}")