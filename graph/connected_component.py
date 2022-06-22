import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().strip().split(' '))

graph = defaultdict(list)

for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().strip().split(' '))
    graph[node1].append(node2)
    graph[node2].append(node1)

def find_comp_dfs(node, component):
    for incident in graph[node]:
        if incident not in component:
            component.append(incident)
            find_comp_dfs(incident, component)

def find_components():
    visited = []
    components = []
    for node in range(1, n+1):
        if node not in visited:
            component = []
            find_comp_dfs(node, component)
            visited += component
            components.append(component)
    
    return components

print(len(find_components()))
