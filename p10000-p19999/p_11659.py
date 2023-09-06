import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
sum_arr = [0]
temp = 0
for k in nums:
    temp += k
    sum_arr.append(temp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(sum_arr[j] - sum_arr[i - 1])
