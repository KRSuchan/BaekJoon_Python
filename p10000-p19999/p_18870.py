# 18870

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr_set = set(arr)
list_arr_set = list(arr_set)
sorted_list_arr_set = sorted(list_arr_set)
dic = {sorted_list_arr_set[i]: i for i in range(len(sorted_list_arr_set))}
for i in arr:
    print(dic[i], end=" ")
