def fac(n):
    if n == 0:
        return 1
    elif n >= 1:
        return n * fac(n-1)
    else:
        return "다시"


def per(n, r):
    if n < r:
        return "다시"
    res = 1
    for i in range(n-r+1, n+1):
        res *= i
    return res

def com(n,r):
    return per(n,r)/fac(r)

print(com(4,2))

