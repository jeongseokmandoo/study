N = int(input())

def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n - 1)
    
fac_N = str(fac(N))

result = 0
for i in range(len(fac_N) - 1, -1, -1):
    if fac_N[i] == '0':
        result += 1
    else:
        break

print(result)