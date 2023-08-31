import sys

coin = []
count = 0
N, K = map(int, sys.stdin.readline().rstrip().split())
for i in range(N):
    coin.append(int(sys.stdin.readline().rstrip()))
for i in reversed(range(N)):
    count += K // coin[i]
    K = K % coin[i]
print(count)
