import sys

input = sys.stdin.readline

dic = {}
N, M = map(int, input().rstrip().split())
for i in range(N):
    site, pwd = input().rstrip().split()
    dic[site] = pwd
for i in range(M):
    print(dic[input().rstrip()])
