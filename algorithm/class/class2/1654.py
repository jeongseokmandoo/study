import sys
input = sys.stdin.readline

k, n = map(int, input().split())
data_list = []
length = 0
for _ in range(k):
    data = int(input().strip())
    data_list.append(data)
    length += data

value = int(length // n)
if value <= 2**31 - 1:
    pass
else:
    value = 2**31 - 1

count = 0
while value > 0:
    for data in data_list:
        count += data // value
    if count >= n:
        print(value)
        break
    value -= 1   
    count = 0     

