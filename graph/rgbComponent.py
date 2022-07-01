#https://www.acmicpc.net/problem/10026

import sys

n = int(sys.stdin.readline().strip())
rgb = []

for _ in range(n):
    rgb.append(list(sys.stdin.readline().strip()))


def adjacency_abnormality(row, col, color):
    adjacency = []
    if color == 'R' or color == 'G':
        if row != 0 and (rgb[row-1][col] == 'R' or rgb[row-1][col] == 'G'):
            adjacency.append((row-1, col))
        if row != n - 1 and (rgb[row+1][col] == 'R' or rgb[row+1][col] == 'G'):
            adjacency.append((row+1, col))
        if col != 0 and (rgb[row][col - 1] == 'R' or rgb[row][col-1] == 'G'):
            adjacency.append((row, col - 1))
        if col != n - 1 and (rgb[row][col + 1] == 'R' or rgb[row][col+1] == 'G'):
            adjacency.append((row, col + 1))
        return adjacency
    else:
        return adjacency_normal(row, col, color)


def adjacency_normal(row, col, color):
    adjacency = []
    if row != 0 and rgb[row-1][col] == color:
        adjacency.append((row-1, col))
    if row != n - 1 and rgb[row+1][col] == color:
        adjacency.append((row+1, col))
    if col != 0 and rgb[row][col-1] == color:
        adjacency.append((row, col-1))
    if col != n - 1 and rgb[row][col+1] == color:
        adjacency.append((row, col+1))

    return adjacency


def normal(root):
    layer = [[root]]
    current = 0

    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            r = next[0]
            c = next[1]
            for adjac in adjacency_normal(r, c, rgb[r][c]):
                if visited_normal[adjac[0]][adjac[1]] == 0:
                    visited_normal[adjac[0]][adjac[1]] = 1
                    layer[current+1].append(adjac)
        current += 1


def abnormality(root):
    layer = [[root]]
    current = 0

    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            r = next[0]
            c = next[1]
            for adjac in adjacency_abnormality(r, c, rgb[r][c]):
                if visited_abnormality[adjac[0]][adjac[1]] == 0:
                    visited_abnormality[adjac[0]][adjac[1]] = 1
                    layer[current + 1].append(adjac)
        current += 1


visited_normal = [[0]*n for _ in range(n)]
visited_abnormality = [[0]*n for _ in range(n)]
normal_cnt = 0
abnormality_cnt = 0

for i in range(n):
    for j in range(n):
        if visited_normal[i][j] == 0:
            normal((i, j))
            normal_cnt += 1

for i in range(n):
    for j in range(n):
        if visited_abnormality[i][j] == 0:
            abnormality((i, j))
            abnormality_cnt += 1


print(str(normal_cnt) + " " + str(abnormality_cnt))