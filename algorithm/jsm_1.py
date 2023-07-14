n = int(input())
d = [input().split(' ') for _ in range(n)]

# print(d)

for i in range(n):
    a = 1
    for j in range(n):
        if int(d[i][0]) < int(d[j][0]):
            if int(d[i][1]) < int(d[j][1]):
                a += 1
    print(a, end=' ')