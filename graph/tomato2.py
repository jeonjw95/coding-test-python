import sys

m, n, h = map(int, sys.stdin.readline().strip().split(' '))

box = [[] for _ in range(h)]

for height in range(h):
    for row in range(n):
        box[height].append(list(map(int, sys.stdin.readline().strip().split(' '))))


def get_incidents(height, row, col):
    incidents = []

    if row != 0 and box[height][row-1][col] == 0:
        incidents.append((height, row-1, col))
    if row != n-1 and box[height][row+1][col] == 0:
        incidents.append((height, row+1, col))
    if col != 0 and box[height][row][col-1] == 0:
        incidents.append((height, row, col-1))
    if col != m-1 and box[height][row][col+1] == 0:
        incidents.append((height, row, col+1))
    if height != 0 and box[height-1][row][col] == 0:
        incidents.append((height-1, row, col))
    if height != h-1 and box[height+1][row][col] == 0:
        incidents.append((height+1, row, col))

    return incidents


def bfs():
    visited = 0
    layer = [[]]
    current = 0

    for height in range(h):
        for row in range(n):
            for col in range(m):
                if box[height][row][col] == 1:
                    layer[current].append((height, row, col))
                    visited += 1
                elif box[height][row][col] == -1:
                    visited += 1

    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            height = next[0]
            row = next[1]
            col = next[2]
            for incident in get_incidents(height, row, col):
                box[incident[0]][incident[1]][incident[2]] = 1
                visited += 1
                layer[current+1].append(incident)
        current += 1

    if visited != m*n*h:
        return -1

    return current - 1


print(bfs())
