n = int(input())
test_case = [input() for _ in range(n)]


for i in test_case:
    score = 0
    sum = 0
    for j in i:
        if j == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)