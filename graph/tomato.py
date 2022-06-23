import sys

m, n = map(int, sys.stdin.readline().strip().split(' '))

box = list()
for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split(' ')))
    box.append(row)


def get_incident(row, col):
    incidents = list()

    if row != 0 and box[row-1][col] == 0:
        incidents.append((row-1, col))
    if row != n-1 and box[row+1][col] == 0:
        incidents.append((row+1, col))
    if col != 0 and box[row][col-1] == 0:
        incidents.append((row, col-1))
    if col != m-1 and box[row][col+1] == 0:
        incidents.append((row, col+1))

    return incidents


def bfs():
    layer = [[]]
    current = 0
    visited = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                layer[current].append((i, j))
                visited += 1
            elif box[i][j] == -1:
                visited += 1
    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            row = next[0]
            col = next[1]
            for incident in get_incident(row, col):
                box[incident[0]][incident[1]] = 1
                layer[current + 1].append(incident)
                visited += 1

        current += 1
    if visited != m * n:
        return -1

    return current-1


print(bfs())


