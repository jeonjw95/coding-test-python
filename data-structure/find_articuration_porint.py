import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
v, e = map(int, sys.stdin.readline().strip().split(' '))
graph = defaultdict(list)
graph[0] = []
for _ in range(e):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

dfn = [-1 for i in range(v+1)]
low = [0 for i in range(v+1)]
visited = [0 for i in range(v+1)]
is_root = [0 for i in range(v+1)]
root_child = defaultdict(int)

num = 1


def dfs(u, p):
    global num
    dfn[u] = num
    low[u] = num
    visited[u] = 1
    num += 1
    for w in graph[u]:
        if is_root[u] == 1 and visited[w] == 0:
            root_child[u] += 1
        if dfn[w] < 0:
            dfs(w, u)
            low[u] = min(low[u], low[w])
        elif w != p:
            low[u] = min(low[u], dfn[w])


for i in range(1, v+1):
    if visited[i] == 0 and len(graph[i]):
        is_root[i] = 1
        root_child[i] = 0
        dfs(i, 0)

cnt = 0
articuration = []

for i in range(1, v+1):
    child = False
    if visited[i] == 0:
        continue
    if is_root[i] == 1 and root_child[i] > 1:
        cnt += 1
        articuration.append(i)
        continue
    elif is_root[i] == 1 and root_child[i] == 1:
        continue
    elif len(graph[i]) == 1:
        continue
    elif dfn[i] == low[i]:
        cnt += 1
        articuration.append(i)
    else:
        for j in graph[i]:
            if dfn[i] <= low[j] and dfn[i] < dfn[j]:
                child = True
        if child:
            cnt += 1
            articuration.append(i)


articuration = sorted(articuration)

print(cnt)


for vertex in articuration:
    print(vertex, end=' ')
