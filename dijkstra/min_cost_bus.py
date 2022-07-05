# https://www.acmicpc.net/problem/1916

import sys
import heapq

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
adj = [[] for _ in range(N+1)]
inf = sys.maxsize
cost = [inf for _ in range(N + 1)]

for _ in range(M):
    v, i, w = map(int, sys.stdin.readline().strip().split(' '))
    adj[v].append([i, w])

s, e = map(int, sys.stdin.readline().strip().split(' '))


def dijkstra(start):
    heap = []
    cost[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        c, n = heapq.heappop(heap)
        if cost[n] < c:
            continue
        for node, weight in adj[n]:
            new_cost = c + weight
            if cost[node] > new_cost:
                cost[node] = new_cost
                heapq.heappush(heap, [new_cost, node])


dijkstra(s)
print(cost[e])
