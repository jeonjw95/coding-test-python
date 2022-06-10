# import collections
# import heapq
# import sys
#
#
# n, m = map(int,input().split())
# graph = collections.defaultdict(list)
# visited = [0] * (n+1)
#
# for i in range(m):
#     weight, u, v = map(int, sys.stdin.readline().strip().split(' '))
#     graph[u].append([weight, u, v])
#     graph[v].append([weight, v, u])
#
# print(graph[1])
# heapq.heapify(graph[1])
# print(graph[1])

test = [1, 2]
test.pop(0)
print(test)
test.pop(0)
print(test)