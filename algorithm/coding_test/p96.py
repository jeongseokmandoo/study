n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

min_list = list()
for j in range(len(data)):
    min_list.append(min(data[j]))

result = max(min_list)

print(result)