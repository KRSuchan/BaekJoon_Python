import sys

arr = []
height = 0
N, M, B = map(int, input().split())

for i in range(N):
    arr.append([int(x) for x in sys.stdin.readline().rstrip().split()])

ans = int(1e9)

for i in range(257):
    need_block = 0
    get_block = B
    for x in range(N):
        for y in range(M):
            if arr[x][y] > i:
                get_block += arr[x][y] - i
            else:
                need_block += i - arr[x][y]
    if need_block > get_block:
        continue
    time = (get_block - B) * 2 + need_block
    if time <= ans:
        height = i
        ans = time

print(ans, height)
