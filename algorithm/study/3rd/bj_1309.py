n = int(input())

def ZeroCase(h):
    if h == 1:
        return 1
    else:
        return (ZeroCase(h - 1) + LeftCase(h - 1) + RightCase(h - 1))

def LeftCase(h):
    if h == 1:
        return 1
    else:
        return(ZeroCase(h - 1) + RightCase(h - 1))

def RightCase(h):
    if h == 1:
        return 1
    else:
        return(ZeroCase(h - 1) + LeftCase(h - 1))

def NumberOfCase(h):
    return (ZeroCase(h) + LeftCase(h) + RightCase(h))

print(NumberOfCase(n))