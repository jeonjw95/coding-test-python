import sys

n = int(sys.stdin.readline().strip())
insertion = []

for _ in range(n):
    (x, y) = map(int, sys.stdin.readline().strip().split(' '))
    if len(insertion) == 0:
        insertion.append()
    else:
        for i in range(insertion):
            if