import sys
input=sys.stdin.readline

n = int(input())

n_list = list()
for _ in range(n):
    n_list.append(list(map(int, input().split())))

n_list.sort(key=lambda x: (x[0], x[1]))   

for i in n_list:
    print(i[0], i[1])
