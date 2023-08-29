from collections import deque

x = int(input())
deq = deque()
times = 1
top = 0
ans = ""
for i in range(x):
    n = int(input())
    for j in range(times, n + 1):
        deq.append(times)
        times += 1
        ans += "+\n"
    if deq[-1] == n:
        deq.pop()
        ans += "-\n"
    else:
        ans = "NO\n"
        break
print(ans)
