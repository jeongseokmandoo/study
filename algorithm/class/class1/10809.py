s = list(input())

en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result_li = list()
for _ in range(len(en)):
    result_li.append(-1)

for i in range(len(s)):
    if result_li[en.index(s[i])] != -1:
        continue
    for j in range(len(en)):
        if en[j] == s[i]:
            result_li[j] = i
            break

for i in result_li:
    print(i, end=' ')

# 겁나 비효율적

s = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')