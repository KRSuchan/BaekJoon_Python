# 1074

N, r, c = map(int, input().split())


def z_searcher(N, r, c):
    if N == 0:
        return 0
    else:
        return 2 * (r % 2) + (c % 2) + 4 * z_searcher(N - 1, int(r / 2), int(c / 2))


print(z_searcher(N, r, c))
