n, k = map(int, input().split())
d = input().split()

d_dict = dict()
d_li = list()
result = 0

for i in d: # 앞으로 더 꽂을 거 있는지 판단하기 위함
    d_dict[i] = 0
for i in d:
    d_dict[i] += 1

for i in range(len(d)):
    val_i = d[i]

    if (val_i in d_li): # 이미 꽂혀 있을 때
        d_dict[val_i] -= 1
        continue

    if (len(d_li) < n): # 꽂을 자리 남아 있을 때
        d_li.append(val_i)
        d_dict[val_i] -= 1
        continue
  
    result += 1 # 자리가 꽉 차 있고 이미 꽂혀 있지 않을 때, 한 번 counting
    for j in d_li: # 앞으로 더 이상 꽂을 거 없는게 있을 때 해당 값을 제거함
        if d_dict[j] == 0:
            d_li.remove(j)
            d_li.append(val_i)
            d_dict[val_i] -=1
            break
    else: #나머지 리스트에서 가장 나중에 있는 값을 제거함
        d_li_li = list()
        for k in d_li:
            d_li_li.append(d[i+1:].index(k))
        d_li[d_li_li.index(max(d_li_li))] = val_i
        d_dict[val_i] -=1

print(result)