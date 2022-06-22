import sys

t = int(sys.stdin.readline().strip())


def find_adjacency(row, col, cabbages):
    adjacency = []
    
    if row != 0 and (row-1, col) in cabbages:
        adjacency.append((row-1, col))
    if row != cabbages[0][0]-1 and (row+1, col) in cabbages:
        adjacency.append((row+1, col))
    if col != 0 and (row, col-1) in cabbages:
        adjacency.append((row, col-1))
    if col != cabbages[0][1] and (row, col+1) in cabbages:
        adjacency.append((row, col+1))
    
    return adjacency

def find_comp_bfs(row, col, cabbages):
    layer = [[(row, col)]]
    visited = [(row, col)]
    current = 0
    
    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            for incident in find_adjacency(next[0], next[1], cabbages):
                if incident not in visited:
                    visited.append(incident)
                    layer[current+1].append(incident)
        current += 1
    
    return visited
    

for _ in range(t):
    col, row, n = map(int, sys.stdin.readline().strip().split(' '))
    cabbages = [(col, row)]
    visited = []
    cnt = 0
    
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        cabbages.append((x, y))
        
    for i, cab in enumerate(cabbages):
        if i == 0:
            continue
        if cab not in visited:
            compo = find_comp_bfs(cab[0], cab[1], cabbages)
            visited += compo
            cnt += 1
    print(cnt)