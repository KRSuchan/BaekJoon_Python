import sys

dic = {}
pocketCnt, quizCnt = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, pocketCnt + 1):
    name = sys.stdin.readline().rstrip()
    dic[i] = name
    dic[name] = i
for _ in range(quizCnt):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isdigit():
        print(dic[int(quiz)])
    else:
        print(dic[quiz])
