import sys

n = int(sys.stdin.readline().strip())
minuntes = list(map(int, sys.stdin.readline().strip().split(' ')))
total = 0
totals = []
for i in range(n):
    tmp = min(minuntes)
    total += tmp
    totals.append(total)
    minuntes.remove(tmp)

print(sum(totals))