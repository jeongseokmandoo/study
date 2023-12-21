import sys

def halfUp(val):
    if val - int(val) >= 0.5 :
        return int(val) + 1
    else:
        return int(val)

n = int(sys.stdin.readline().strip())
if n == 0:
    print(0)
else:
    rate = list(int(sys.stdin.readline().strip()) for _ in range(n))
    rate.sort()

    len_total = len(rate)

    num = halfUp(len_total * 0.15)

    if num > 0:
        avr = sum(rate[num:-num]) / len(rate[num:-num])
    else:
        avr = sum(rate) / len(rate)

    value = halfUp(avr)

    print(value)