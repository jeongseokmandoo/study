n = input()
int_n = int(n)

if '7' in n:
    if int_n % 7 == 0:
        print(3)
    else:
        print(2)
else:
    if int_n % 7 == 0:
        print(1)
    else:
        print(0)