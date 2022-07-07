# https://www.acmicpc.net/problem/13549

import sys
from collections import deque

MAX = 100001
n, k = map(int, sys.stdin.readline().strip().split(' '))
dist = [0 for _ in range(MAX)]
visited = [False for _ in range(MAX)]

q = deque()
q.append(n)
visited[n] = True
dist[n] = 0

while q:
    current = q.popleft()
    if 0 <= current*2 < MAX and visited[current*2] is False:
        dist[current*2] = dist[current]
        visited[current*2] = True
        q.appendleft(current*2)
    if 0 <= current + 1 < MAX and visited[current+1] is False:
        dist[current+1] = dist[current] + 1
        visited[current+1] = True
        q.append(current+1)
    if 0 <= current - 1 < MAX and visited[current-1] is False:
        dist[current-1] = dist[current] + 1
        visited[current-1] = True
        q.append(current-1)


print(dist[k])