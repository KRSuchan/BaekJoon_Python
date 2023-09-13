import sys
from collections import deque


def bfs(V):
    queue = deque()
    queue.append(V)
    visited_1[V] = 1
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if graph[v][i] == 1 and visited_1[i] == 0:
                queue.append(i)
                visited_1[i] = 1


def dfs(V):
    print(V, end=" ")
    visited_2[V] = 1
    for i in range(1, N + 1):
        if graph[V][i] == 1 and visited_2[i] == 0:
            dfs(i)


N, M, V = map(int, sys.stdin.readline().rstrip().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    # 연결 관계 형성
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

# 방문 여부 생성
visited_1 = [0] * (N + 1)
visited_2 = [0] * (N + 1)

dfs(V)
print()
bfs(V)
