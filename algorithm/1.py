memo=[0]*101
def f(n):
    print(n, end=" ")
    if memo[n]!=0:
        return memo[n]
    else:
        if n==1 or n==2:
            memo[n]=1
            return 1
        else:
            tmp = f(n-1)+f(n-2)
            memo[n] = tmp
            return tmp

print(f(100))
