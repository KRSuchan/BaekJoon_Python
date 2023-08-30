import sys

times = int(sys.stdin.readline())
S = set()

for _ in range(times):
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        operator, x = temp[0], int(temp[1])
        if operator == "add":
            S.add(x)
        elif operator == "remove":
            S.discard(x)
        elif operator == "check":
            print(1 if x in S else 0)
        elif operator == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
