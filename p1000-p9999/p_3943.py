# p_3943 : 헤일스톤 수열
import sys

input = sys.stdin.readline()
T = int(input())
for _ in range(T):
    n = int(input())
    res = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        res = max(res, n)
    print(res)
