# https://www.acmicpc.net/problem/1238

import sys
import heapq

N, M, X = map(int, sys.stdin.readline().strip().split(' '))
adj = [[] for _ in range(N+1)]
inf = sys.maxsize

for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().strip().split(' '))
    adj[s].append([e, t])


def dijkstra(start, end):
    if start == end:
        return 0
    heap = []
    dist = [inf for _ in range(N+1)]
    dist[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        weight, node = heapq.heappop(heap)

        for n, w in adj[node]:
            new_weight = weight + w
            if new_weight < dist[n]:
                dist[n] = new_weight
                heapq.heappush(heap, [new_weight, n])

    return dist[end]


maxi = 0
for i in range(1, N+1):
    tmp = dijkstra(i, X) + dijkstra(X, i)
    maxi = max(maxi, tmp)


print(maxi)