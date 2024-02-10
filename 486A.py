def zena(n):
    if n % 2 ==0:
        return n /2
    return -(n//2 + 1)
n = int(input())
y = int(zena(n))
print(y)