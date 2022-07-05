# https://www.acmicpc.net/problem/1753

import sys, heapq

V, E = map(int, sys.stdin.readline().strip().split(' '))
start = int(sys.stdin.readline().strip())
adj = [[] for _ in range(V+1)]
inf = "INF"

for _ in range(E):
    v, i, w = map(int, sys.stdin.readline().strip().split(' '))
    adj[v].append([i, w])


def dijkstra(s):
    heap = []
    dist = [inf for _ in range(V+1)]
    dist[s] = 0
    heapq.heappush(heap, [0, s])

    while heap:
        cost, node = heapq.heappop(heap)
        for n, w in adj[node]:
            new_cost = cost + w
            if dist[n] == inf or dist[n] > new_cost:
                dist[n] = new_cost
                heapq.heappush(heap, [new_cost, n])

    return dist[1:]


for w in dijkstra(start):
    print(w)