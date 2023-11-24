import sys

sys.setrecursionlimit(10**9)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for i in range(N + 1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0  # Connected Component 수
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1
print(count)
