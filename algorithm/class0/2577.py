n = 1
for _ in range(3):
    num = int(input())
    n = n * num
n = str(n)

n_li = list()
for _ in range(10):
    n_li.append(0)

for i in n:
    n_li[int(i)] += 1

for i in n_li:
    print(i)