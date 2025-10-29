N = int(input())
room = [input().strip() for _ in range(N)]

def count_horizontal(room):
    count = 0
    for row in room:
        empty = 0
        for cell in row:
            if cell == '.':
                empty += 1
            else:
                if empty >= 2:
                    count += 1
                empty = 0
        if empty >= 2:
            count += 1
    return count

def count_vertical(room):
    count = 0
    for col in range(N):
        empty = 0
        for row in range(N):
            if room[row][col] == '.':
                empty += 1
            else:
                if empty >= 2:
                    count += 1
                empty = 0
        if empty >= 2:
            count += 1
    return count

horiz = count_horizontal(room)
vert = count_vertical(room)
print(horiz, vert)
