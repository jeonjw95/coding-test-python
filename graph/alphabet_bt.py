# https://www.acmicpc.net/problem/1987

import sys

r, c = map(int, sys.stdin.readline().strip().split(' '))
alphabet = []
visited = [0] * 26
length = []
maxi = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(r):
    alphabet.append(list(sys.stdin.readline().strip()))


def find_adjacency(row, col):
    adjacency = []
    if row != 0 and visited[ord(alphabet[row-1][col]) - 65] == 0:
        adjacency.append((row-1, col))
    if row != r - 1 and visited[ord(alphabet[row+1][col]) - 65] == 0:
        adjacency.append((row+1, col))
    if col != 0 and visited[ord(alphabet[row][col-1]) - 65] == 0:
        adjacency.append((row, col-1))
    if col != c - 1 and visited[ord(alphabet[row][col+1]) - 65] == 0:
        adjacency.append((row, col+1))
    return adjacency


def bt(row, col, cnt):
    global maxi
    maxi = max(cnt, maxi)
    # adjacency = find_adjacency(row, col)
    for i in range(4):
        nr = row + dx[i]
        nc = col + dy[i]
        if 0 <= nr <= r-1 and 0 <= nc <= c-1 and visited[ord(alphabet[nr][nc]) - 65] == 0:
            visited[ord(alphabet[nr][nc]) - 65] = 1
            bt(nr, nc, cnt+1)
            visited[ord(alphabet[nr][nc]) - 65] = 0


visited[ord(alphabet[0][0]) - 65] = 1
bt(0, 0, 1)
print(maxi)


# def find_adjacency(row, col, i):
#     adjacency = []
#     if row != 0 and alphabet[row-1][col] not in visited[0][i]:
#         adjacency.append((row-1, col))
#     if row != r - 1 and alphabet[row+1][col] not in visited[0][i]:
#         adjacency.append((row+1, col))
#     if col != 0 and alphabet[row][col-1] not in visited[0][i]:
#         adjacency.append((row, col-1))
#     if col != c -1 and alphabet[row][col+1] not in visited[0][i]:
#         adjacency.append((row, col+1))
#     return adjacency


# def bfs(root):
#     layer = [[root]]
#     current = 0
#     visited.append([[alphabet[root[0]][root[1]]]])
#
#     while len(layer[current]):
#         layer.append([])
#         visited.append([])
#         print(visited)
#         for i, next in enumerate(layer[current]):
#             row = next[0]
#             col = next[1]
#             for j, adjac in enumerate(find_adjacency(row, col, current, i)):
#                 layer[current+1].append(adjac)
#                 visited[current+1].append(visited[current][i] + [alphabet[adjac[0]][adjac[1]]])
#
#         if current != 0:
#             print("pop:" + str(visited.pop(current-1)))
#
#         current += 1
#
#     return current

# def bfs(root):
#     layer = [[root]]
#     current = 0
#     visited.append([[alphabet[root[0]][root[1]]]])
#
#     while len(layer[0]):
#         layer.append([])
#         visited.append([])
#         for i, next in enumerate(layer[0]):
#             row = next[0]
#             col = next[1]
#             for j, adjac in enumerate(find_adjacency(row, col, i)):
#                 layer[1].append(adjac)
#                 visited[1].append(visited[0][i] + [alphabet[adjac[0]][adjac[1]]])
#
#         visited.pop(0)
#         layer.pop(0)
#
#         current += 1
#
#     return current


