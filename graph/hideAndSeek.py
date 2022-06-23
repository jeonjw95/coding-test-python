import sys

start, end = map(int, sys.stdin.readline().strip().split(' '))


def get_incidents(pos):
    incidents = []

    if pos != 0:
        incidents.append(pos - 1)
    if pos != 100000:
        incidents.append(pos + 1)
    if pos*2 <= 100000:
        incidents.append(pos * 2)

    return incidents


def bfs():
    layer = [[start]]
    current = 0
    visited = [0 for _ in range(100001)]
    if start == end:
        return 0
    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            for incident in get_incidents(next):
                if incident == end:
                    return current + 1
                if visited[incident] == 0:
                    layer[current+1].append(incident)
                    visited[incident] = visited[next] + 1
        current += 1


print(bfs())
