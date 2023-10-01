import sys

N = int(sys.stdin.readline().rstrip())
P = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
white = 0
blue = 0


def sol(x, y, T):
    global white, blue
    c = P[x][y]
    for i in range(x, x + T):
        for j in range(y, y + T):
            if c != P[i][j]:
                sol(x, y, T // 2)
                sol(x, y + T // 2, T // 2)
                sol(x + T // 2, y, T // 2)
                sol(x + T // 2, y + T // 2, T // 2)
                return
    if c == 0:
        white += 1
    else:
        blue += 1


sol(0, 0, N)
print(white)
print(blue)
