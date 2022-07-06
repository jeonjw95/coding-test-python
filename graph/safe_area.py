# https://www.acmicpc.net/problem/2468

import sys

N = int(sys.stdin.readline().strip())
area = []

for _ in range(N):
    area.append(list(map(int, sys.stdin.readline().strip().split(' '))))


def bfs(start, height):
    q = [start]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        row, col = q.pop(0)
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] is False and area[nr][nc] > height:
                visited[nr][nc] = True
                q.append((nr, nc))


maxi = 0
for h in range(0, 101):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] is False and area[i][j] > h:
                bfs((i, j), h)
                cnt += 1

    maxi = max(cnt, maxi)
    if cnt == 0:
        break

print(maxi)