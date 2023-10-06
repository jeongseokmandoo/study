word = list(input())

for i in range(len(word)):
    word[i] = word[i].upper()

word_list = list(set(word))
num_list = list()
for i in range(len(word_list)):
    num_list.append(0)

for i in range(len(word_list)):
    for j in word:
        if word_list[i] == j:
            num_list[i] = num_list[i] + 1

num_li = sorted(num_list)
if num_li[-1] == num_li[-2]:
    print("?")
else:
    print(word_list[num_list.index(max(num_list))])

# 런타임 오류 뜸

word = input().lower()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))].upper())
    

    


