import sys
import heapq

inf = 10000000

graph = [
    #1, 2, 3, 4, 5, 6
    [0, 2, 5, 1, inf, inf],
    [2, 0, 3, 2, inf, inf],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, inf],
    [inf, inf, 1, 1, 0, 2],
    [inf, inf, 5, inf, 2, 0]
]
adj = [
    [],
    [[2, 2], [3, 5], [4, 1]],
    [[1, 2], [4, 2], [3, 3]],
    [[2, 3], [1, 5], [4, 3], [5, 1], [6, 5]],
    [[1, 1], [2, 2], [3, 3], [5, 1]],
    [[4, 1], [3, 1], [6, 2]],
    [[5, 2], [3, 5]]
]


def dijkstra(start):
    heap = []
    d = [inf for _ in range(6)]
    v = [False for _ in range(len(d))]
    d[start-1] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        cost, node = heapq.heappop(heap)
        for n, c in adj[node]:
            new_cost = cost + c
            if d[n-1] > new_cost:
                d[n-1] = new_cost
                heapq.heappush(heap, [new_cost, n])

    return d


print(dijkstra(1))


