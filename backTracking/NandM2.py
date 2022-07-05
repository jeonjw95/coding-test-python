# https://www.acmicpc.net/problem/15650

import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
coll = []    # set의 리스트로 중복을 제거
visited = []


def bt():
    if len(visited) == M:
        num_set = set(visited)
        if num_set not in coll:
            print(' '.join(map(str, visited)))
            coll.append(num_set)
        return
    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            bt()
            visited.pop()


bt()