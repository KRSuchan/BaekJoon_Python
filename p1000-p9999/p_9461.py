import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    C = int(sys.stdin.readline())
    padovan = [0, 1, 1, 1, 2, 2]
    if C > 5:
        for i in range(6, C + 1):
            padovan.append(padovan[i - 1] + padovan[i - 5])
        print(padovan[C])
    else:
        print(padovan[C])
