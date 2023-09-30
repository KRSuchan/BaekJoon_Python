import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []

for i in range(N):
    number = int(sys.stdin.readline().rstrip())
    if number == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, number)
