# import sys
# input=sys.stdin.readline

# n = int(input())

# n_list = list()
# for _ in range(n):
#     n_list.append(list(map(int, input().split())))

# n_list.sort(key=lambda x: (x[0], x[1]))   

# for i in n_list:
#     print(i[0], i[1])

import sys
input = sys.stdin.readline
output = sys.stdout.write

# 점의 개수 N 입력
n = int(input().strip())

# 점들을 저장할 리스트 생성 및 입력 받기
n_list = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 점들을 정렬 (x좌표 -> y좌표 순으로)
n_list.sort()

# 결과 출력
output('\n'.join(f"{x} {y}" for x, y in n_list) + '\n')
