# p_3595 : 맥주 냉장고
import sys

input = sys.stdin.readline
n = int(input())
ans = ""
mi = 1e8
for i in range(1, n + 1):
    if i ** 3 > n: break
    if n % i == 0:
        x = n // i
        for j in range(1, x + 1):
            if j ** 2 > x: break
            if x % j == 0:
                k = x // j
                size = i * j + i * k + j * k
                if size < mi:
                    mi = size
                    ans = f"{i} {j} {k}"
print(ans)
