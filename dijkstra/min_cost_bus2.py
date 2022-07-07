# https://www.acmicpc.net/problem/11779

import sys
import heapq

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
adj = [[] for _ in range(n+1)]
inf = sys.maxsize

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().strip().split(' '))
    adj[s].append([e, c])

start, end = map(int, sys.stdin.readline().strip().split(' '))
dist = [inf for _ in range(n + 1)]
near = [start for _ in range(n + 1)]


def dijkstra():
    heap = []
    dist[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for next, nextCost in adj[node]:
            new_cost = cost + nextCost
            if dist[next] > new_cost:
                dist[next] = new_cost
                near[next] = node
                heapq.heappush(heap, [new_cost, next])


dijkstra()
print(dist[end])

tmp = end
ans = []
while start != tmp:
    ans.append(str(tmp))
    tmp = near[tmp]

ans.append(str(start))
ans.reverse()
print(len(ans))
print(' '.join(ans))

