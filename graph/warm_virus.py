import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = defaultdict(list)

for _ in range(m):
    com1, com2 = map(int, sys.stdin.readline().strip().split(' '))
    graph[com1].append(com2)
    graph[com2].append(com1)
    
def find_component_bfs(node):
    component = []
    layer = [[node]]
    current = 0
    
    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            for incident in graph[next]:
                if incident not in component:
                    component.append(incident)
                    layer[current+1].append(incident)
        current += 1
                    
    return len(component)

print(find_component_bfs(1)-1)