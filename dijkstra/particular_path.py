# https://www.acmicpc.net/problem/1504

import sys
import heapq

N, E = map(int, sys.stdin.readline().strip().split(' '))
adj = [[] for _ in range(N+1)]
inf = sys.maxsize


for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().strip().split(' '))
    adj[v1].append([v2, w])
    adj[v2].append([v1, w])

a, b = map(int, sys.stdin.readline().strip().split(' '))


def dijkstra(s, e):
    dist = [inf for _ in range(N + 1)]
    heap = []
    dist[s] = 0
    heapq.heappush(heap, [0, s])

    while heap:
        cost, current = heapq.heappop(heap)
        if cost > dist[current]:
            continue
        for next, next_cost in adj[current]:
            new_cost = cost + next_cost
            if new_cost < dist[next]:
                dist[next] = new_cost
                heapq.heappush(heap, [new_cost, next])

    return dist[e]


case1 = dijkstra(1, a) + dijkstra(a, b) + dijkstra(b, N)
case2 = dijkstra(1, b) + dijkstra(b, a) + dijkstra(a, N)

mini = min(case1, case2)

if mini >= inf:
    print(-1)
else:
    print(mini)
