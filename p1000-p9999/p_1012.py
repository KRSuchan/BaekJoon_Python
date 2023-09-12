import sys
from collections import deque


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    # while queue is empty
    while queue:
        a, b = queue.popleft()
        for t in range(4):
            nx = a + dx[t]
            ny = b + dy[t]
            # out of size
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            # 이동 반경
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return


# Test Case count
T = int(sys.stdin.readline().rstrip())

# x, y 주변 변화량
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    # M : width, N : Height, K : Pos_Cnt
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0] * N for _ in range(M)]
    # cnt : 지렁이 수
    cnt = 0
    for i in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x][y] = 1
    # bfs start
    for j in range(M):
        for k in range(N):
            if graph[j][k] == 1:
                bfs(j, k)
                cnt += 1
    print(cnt)
