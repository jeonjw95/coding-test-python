import heapq
import sys

n = int(sys.stdin.readline().strip())
plus_heap = []
minus_heap = []
for _ in range(n):
    arg = int(sys.stdin.readline().strip())
    if arg == 0:
        if not (len(plus_heap) or len(minus_heap)):
            print(0)
        elif not len(plus_heap):
            print(-heapq.heappop(minus_heap))
        elif not len(minus_heap):
            print(heapq.heappop(plus_heap))
        elif plus_heap[0] > minus_heap[0]:
            print(-heapq.heappop(minus_heap))
        elif plus_heap[0] < minus_heap[0]:
            print(heapq.heappop(plus_heap))
        elif plus_heap[0] == minus_heap[0]:
            print(-heapq.heappop(minus_heap))
    elif arg > 0:
        heapq.heappush(plus_heap, arg)
    else:
        heapq.heappush(minus_heap, -arg)

