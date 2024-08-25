# p_30823 : 건공문자열
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = input().rstrip()
if k == 1:
    ans = data
elif (n-k) % 2:
    ans = data[k-1:]+data[:k-1]
else:
    ans = data[k-1:]+data[k-2::-1]
print(ans)
