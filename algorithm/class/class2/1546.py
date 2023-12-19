n = int(input())
score = list(map(int, input().split()))
M = max(score)
sum = 0

for i in range(n):
    sum += score[i] / M * 100

print(sum / n)
