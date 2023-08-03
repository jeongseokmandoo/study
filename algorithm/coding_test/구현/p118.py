n, m = map(int, input().split())
a, b, d = map(int, input().split())
graph = list(input().split() for _ in range(n))

d_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]

count = 0
result = 1
while True:
    if count == 4:
        break
    if d == -1:
        d = 3
    da = a + d_list[d][0]
    db = b + d_list[d][1]
    if da < 0 or da >= n or db < 0 or db >= m:
        d += -1
        count += 1
        continue
    if int(graph[da][db]) == 1:
        d += -1
        count += 1
        continue
    graph[a][b] = '1'
    a, b = da, db
    result += 1
    
print(result)