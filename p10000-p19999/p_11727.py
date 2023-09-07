import sys

n = int(sys.stdin.readline().rstrip())
tile = [0] * 1001
tile[1] = 1
tile[2] = 3

if n < 3:
    print(tile[n])
else:
    for i in range(3, n + 1):
        tile[i] = (tile[i - 1] + 2 * tile[i - 2]) % 10007
    print(tile[n])
