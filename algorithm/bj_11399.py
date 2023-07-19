n = int(input())
d = input().split(' ')

for i in range(0, len(d)):
    d[i] = int(d[i])

d.sort()

result = 0
for i in range(1, len(d) + 1):
    result += d[-i] * (i)

print(result)