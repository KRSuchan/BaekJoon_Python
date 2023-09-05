import sys

T = int(sys.stdin.readline().rstrip())


for _ in range(T):
    C = int(sys.stdin.readline().rstrip())
    dic = {}
    for _ in range(C):
        clothes = list(sys.stdin.readline().rstrip().split())
        if clothes[1] in dic:
            dic[clothes[1]].append(clothes[0])
        else:
            dic[clothes[1]] = [clothes[0]]
    cnt = 1
    for i in dic:
        cnt *= len(dic[i]) + 1
    print(cnt - 1)
