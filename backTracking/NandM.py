# https://www.acmicpc.net/problem/15649

import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
visited = []


def bt():
    if len(visited) == M:
        print(' '.join(map(str, visited)))
    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            bt()
            visited.pop()


bt()

