# p_20124 : 모르고리즘 회장님 추천 받습니다
import sys

input = sys.stdin.readline
N = int(input())
sts = []
for _ in range(N):
    name, score = input().split()
    sts.append([name, int(score)])
sts.sort(key=lambda x: (-x[1], x[0]))
print(sts[0][0])
