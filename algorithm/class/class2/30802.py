import sys
input = sys.stdin.readline

n = int(input().strip())
amount_list = list(map(int, input().strip().split()))
t, p = map(int, input().split())

t_amount = 0
for amount in amount_list:
    if amount % t == 0:
        t_amount += amount // t
    else:
        t_amount += amount // t + 1

print(t_amount )
print(n // p, n % p)