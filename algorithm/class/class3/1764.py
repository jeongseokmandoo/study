# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# see_list = [input().strip() for _ in range(n)]

# result_list = []

# for _ in range(m):
#     hear = input().strip()
#     if hear in see_list:
#         result_list.append(hear)

# print(len(result_list))
# result_list.sort()
# for result in sorted(result_list):
#     print(result)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
see_set = {input().strip() for _ in range(n)}  # set으로 변환하여 빠른 탐색 가능하게 함

result_set = set()  # 결과를 저장할 set

for _ in range(m):
    hear = input().strip()
    if hear in see_set:  # set을 사용하여 탐색 시간 단축
        result_set.add(hear)

result_list = sorted(result_set)  # 최종 결과 정렬
print(len(result_list))
for result in result_list:
    print(result)
