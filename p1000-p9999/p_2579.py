import sys

input = sys.stdin.readline
array = []
score = []
N = int(input())
for _ in range(N):
    array.append(int(input()))
if N >= 1:
    score.append(array[0])
if N >= 2:
    score.append(max(array[0] + array[1], array[1]))
if N >= 3:
    score.append(max(array[0] + array[2], array[1] + array[2]))
if N > 3:
    for i in range(3, N):
        score.append(
            max(score[i - 2] + array[i], score[i - 3] + array[i - 1] + array[i])
        )
print(score.pop())
