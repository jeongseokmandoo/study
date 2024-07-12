import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data_list = [int(input().strip()) for _ in range(n)]

count = 0
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    count += k // data_list[i]
    k %= data_list[i]

print(count)