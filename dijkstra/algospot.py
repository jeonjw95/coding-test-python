# https://www.acmicpc.net/problem/1261

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split(' '))
spot = []

for _ in range(N):
    spot.append(list(map(int, sys.stdin.readline().strip())))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
dist = [[-1]*M for _ in range(N)]
q = deque()
q.append((0, 0))
dist[0][0] = 0
while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1:
            if spot[nr][nc] == 0:
                dist[nr][nc] = dist[r][c]
                q.appendleft((nr, nc))
            else:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))


print(dist[N-1][M-1])
# def bt(r, c):
#     global cnt
#     global mini
#     if r == N-1 and c == M-1:
#         mini = min(mini, cnt)
#         return
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
#             visited[nr][nc] = True
#             if spot[nr][nc] == 1:
#                 cnt += 1
#             bt(nr, nc)
#             visited[nr][nc] = False
#             if spot[nr][nc] == 1:
#                 cnt -= 1
#
#
# visited[0][0] = True
# bt(0, 0)
# print(mini)
# def bfs():
#     cnt = 0
#     q = deque()
#     q.append([0, 0])
#     visited[0][0] = True
#     dr = [1, -1, 0, 0]
#     dc = [0, 0, 1, -1]
#
#     while q:
#         r, c = q.popleft()
#         for i in range(4):
#             nr = dr[i] + r
#             nc = dc[i] + c
#             if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] is False:
#                 visited[nr][nc] = True
#                 if spot[nr][nc] is 1:
#                     cnt += 1

