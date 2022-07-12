# https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline().strip())
parents = [0 for _ in range(N+1)]
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().strip().split(' '))
    adj[v1].append(v2)
    adj[v2].append(v1)


def dfs(node):
    for child in adj[node]:
        if parents[child] == 0:
            parents[child] = node
            dfs(child)


dfs(1)

for i in range(2, N+1):
    print(parents[i])