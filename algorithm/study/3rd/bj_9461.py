p = [1, 1, 1, 2, 2]
t = int(input())
n = [int(input()) for _ in range(t)]

for i in range(4, max(n)):
    value = p[i] + p[i - 4]
    p.append(value)

for j in n:
    print(p[j - 1])
