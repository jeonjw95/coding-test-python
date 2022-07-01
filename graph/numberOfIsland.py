import sys

def find_adjacency(row, col):
    adjacency = []
    if row != 0:
        if island[row-1][col] == 1:
            adjacency.append((row-1, col))
        if col != 0 and island[row-1][col-1] == 1:
            adjacency.append((row-1, col-1))
        if col != w-1 and island[row-1][col+1] == 1:
            adjacency.append((row-1, col+1))
    if row != h-1:
        if island[row+1][col] == 1:
            adjacency.append((row+1, col))
        if col != 0 and island[row+1][col-1] == 1:
            adjacency.append((row+1, col-1))
        if col != w-1 and island[row+1][col+1] == 1:
            adjacency.append((row+1, col+1))
    if col != 0 and island[row][col-1] == 1:
        adjacency.append((row, col-1))
    if col != w-1 and island[row][col+1] == 1:
        adjacency.append((row, col+1))

    return adjacency


def find_island(root):
    layer = [[root]]
    current = 0
    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            for incident in find_adjacency(next[0], next[1]):
                r = incident[0]
                c = incident[1]
                if visited[r][c] == 0:
                    visited[r][c] = 1
                    layer[current+1].append(incident)
        current += 1


w = 0
h = 0
island = []




while True:
    island = []
    w, h = map(int, sys.stdin.readline().strip().split(' '))
    if w == 0 and h == 0:
        break
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for _ in range(h):
        island.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                find_island((i, j))
                cnt += 1
    print(cnt)



