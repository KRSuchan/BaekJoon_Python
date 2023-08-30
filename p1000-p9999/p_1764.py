import sys

hear = set()
ans = set()
a, b = map(int, sys.stdin.readline().rstrip().split())
for i in range(a):
    hear.add(sys.stdin.readline().rstrip())
for i in range(b):
    see = sys.stdin.readline().rstrip()
    if see in hear:
        ans.add(see)
ans = sorted(ans)
print(len(ans))
for i in ans:
    print(i)
