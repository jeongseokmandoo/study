n = int(input())
li = list()

for i in range(n):
    li.append(i + 1)

count = 0
if n == 1:
    print(1)
else:
    while count < n - 1:
        print(li[0], end=' ')
        del li[0]
        a = li[0]
        li.append(a)
        del li[0]
        count += 1
        if count == n - 1:
            print(li[0])

# import sys

# n = int(sys.stdin.readline())
# card = [i for i in range(1, n + 1)]
# res = []

# while True:
#     res.append(card.pop(0))
#     if not card:
#         break
#     card.append(card.pop(0))

# print(*res)