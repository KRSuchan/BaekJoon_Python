from collections import deque
import sys

input = sys.stdin.readline
N = int(input().rstrip())
V = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
for _ in range(V):
    a, b = map(int, input().rstrip().split())
    graph[a] += [b]
    graph[b] += [a]
visit[1] = 1
deq = deque([1])
while deq:
    c = deq.popleft()
    for nx in graph[c]:
        if visit[nx] == 0:
            deq.append(nx)
            visit[nx] = 1
print(sum(visit) - 1)
