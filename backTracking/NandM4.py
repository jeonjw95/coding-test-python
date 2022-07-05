# https://www.acmicpc.net/problem/15652

import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
visited = []


def bt(start):
    if len(visited) == M:
        print(" ".join(map(str, visited)))
        return
    for i in range(start, N+1):
        visited.append(i)
        bt(i)
        visited.pop()


bt(1)
