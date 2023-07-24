n, k = map(int, input().split())
d = input().split()

d_li = list()
result = 0

for i in range(len(d)):
    val_i = d[i]
    if (val_i in d_li): # 이미 꽂혀 있을 때
        continue

    if (len(d_li) < n): # 꽂을 자리 남아 있을 때
        d_li.append(val_i)
        continue
    
    result += 1 # 자리가 꽉 차 있고 이미 꽂혀 있지 않을 때, 한 번 counting
    for j in d_li: # 앞으로 더 이상 안 꽂아도 되는 게 있을 때 해당 값을 제거함
        if j not in d[i+1:]:
            d_li.remove(j)
            d_li.append(val_i)
            break
    else: #나머지 리스트에서 가장 나중에 있는 값을 제거함
        d_li_li = list()
        for k in d_li:
            d_li_li.append(d[i+1:].index(k))
        d_li[d_li_li.index(max(d_li_li))] = val_i

print(result)