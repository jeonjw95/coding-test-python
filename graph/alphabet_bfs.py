# https://www.acmicpc.net/problem/1987

import sys

R, C = map(int, sys.stdin.readline().strip().split(' '))
alphabet = []
maxi = 1
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(R):
    alphabet.append(list(sys.stdin.readline().strip()))

def bfs(row, col):
    q = set([(row, col, alphabet[row][col])])
    global maxi
    while q:
        r, c, ans = q.pop()
        maxi = max(maxi, len(ans))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and alphabet[nr][nc] not in ans:
                q.add((nr, nc, ans + alphabet[nr][nc]))


bfs(0, 0)
print(maxi)