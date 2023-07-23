n, k = map(int, input().split())
d = input().split()

d_dict = dict()
d_li = list()
result = 0

for i in d:
    d_dict[i] = 0
for i in d:
    d_dict[i] += 1

for i in range(len(d)):
    val_i = d[i]
    if (val_i in d_li):
        d_dict[val_i] -= 1
        continue
    if (len(d_li) < n):
        d_li.append(val_i)
        d_dict[val_i] -= 1
        continue   
    result += 1
    for j in d_li:
        if d_dict[j] == 0:
            d_li.remove(j)
            d_li.append(val_i)
            d_dict[val_i] -=1
            break
    else:
        d_li_li = list()
        for k in d_li:
            d_li_li.append(d[i+1:].index(k))
        d_li[d_li_li.index(max(d_li_li))] = val_i
        d_dict[val_i] -=1

print(result)