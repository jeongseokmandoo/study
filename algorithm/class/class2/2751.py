import sys
input=sys.stdin.readline

n = int(input())
n_list = [int(input()) for _ in range(n)]

# 퀵 정렬 사용
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]

#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)

# n_list = quick_sort(n_list)


# 파이썬 정렬 라이브러리 사용

for i in sorted(n_list):
    print(i)