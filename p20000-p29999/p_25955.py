# p_25955 : APC는 쉬운 난이도 순일까, 아닐까?
n = int(input())
li1 = input().split()
tier = ['B', 'S', 'G', 'P', "D"]
li2 = [0] * n
for i in range(n):
    li2[i] = tier.index(li1[i][0]) * 1000 + (1000 - int(li1[i][1:]))
if li2 == sorted(li2):
    print("OK")
else:
    x = []
    for i in range(n):
        if li2[i] != sorted(li2)[i]:
            x.append(li1[i])
    print("KO")
    print(' '.join(reversed(x)))
