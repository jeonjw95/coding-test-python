import heapq
import sys

n = int(sys.stdin.readline().strip())
heap = []
for _ in range(n):
    arg = int(sys.stdin.readline().strip())
    if arg == 0:
        if not len(heap):
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, arg)

