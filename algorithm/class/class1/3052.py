num = [int(input()) for _ in range(10)]
amount = list()

for i in range(10):
    rest = num[i] % 42
    if rest not in amount:
        amount.append(rest)

print(len(amount))
