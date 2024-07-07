import sys
input = sys.stdin.readline

n ,t = map(int, input().split())
data_list = [tuple(map(int, input().strip().split())) for _ in range(n)]

result_list = []
for data in data_list:
    s = data[0]
    i = data[1]
    c = data[2]
    for _ in range(c):
        if s >= t:
            result_list.append(s - t)
            break
        s += i

print(min(result_list) if result_list else -1)