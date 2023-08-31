import sys

P = int(sys.stdin.readline().rstrip())
people = []
total = 0
people = list(map(int, sys.stdin.readline().rstrip().split()))
people.sort()
for i in range(P):
    term = 0
    for j in range(i + 1):
        term += people[j]
    total += term
print(total)
