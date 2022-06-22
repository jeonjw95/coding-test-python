import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline().strip())
graph = [[] for i in range(n+1)]
dp = [[0, 0] for i in range(n+1)]   #dp[node][0 or 1] 0 == not ealy adoptor, 1 == early adoptor


for _ in range(n-1):
    node1, node2 = map(int, sys.stdin.readline().strip().split(' '))
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [0 for i in range(n+1)]


def find_ealy_adoptor(node):
    global visited
    visited[node] = 1
    dp[node][1] = 1

    for child in graph[node]:
        if visited[child] != 1:
            find_ealy_adoptor(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])


find_ealy_adoptor(1)
print(min(dp[1][0], dp[1][1]))
