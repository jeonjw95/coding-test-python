import sys

def get_incidents(num):
    incidents = []
    if num % 3 == 0:
        incidents.append(num // 3)
    if num % 2 == 0:
        incidents.append(num // 2)
    incidents.append(num-1)

    return incidents


number = int(sys.stdin.readline().strip())


def bfs():
    visited = [0 for _ in range(number + 1)]
    visited[number] = 1
    layer = [[number]]
    current = 0
    if number == 1:
        return 0

    while len(layer[current]):
        layer.append([])
        for next in layer[current]:
            for incident in get_incidents(next):
                if incident == 1:
                    return current + 1
                if visited[incident] == 0:
                    layer[current + 1].append(incident)
                    visited[incident] = 1
        current += 1
    return current


print(bfs())
