# import sys
# input = sys.stdin.readline

# k, n = map(int, input().split())
# data_list = []
# length = 0
# for _ in range(k):
#     data = int(input().strip())
#     data_list.append(data)
#     length += data

# value = int(length // n)
# if value <= 2**31 - 1:
#     pass
# else:
#     value = 2**31 - 1

# count = 0
# while value > 0:
#     for data in data_list:
#         count += data // value
#     if count >= n:
#         print(value)
#         break
#     value -= 1   
#     count = 0     

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
data_list = []
for _ in range(k):
    data = int(input().strip())
    data_list.append(data)

def count_pieces(length):
    count = 0
    for data in data_list:
        count += data // length
    return count

start, end = 1, max(data_list)
answer = 0

while start <= end:
    mid = (start + end) // 2
    if count_pieces(mid) >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
