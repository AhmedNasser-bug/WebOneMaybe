n = int(input())
x = 0
A = 0
while(n > 0 ):
    m = input().split(" ")
    a = int(m[0])
    b = int(m[1]) 
    A += b-a
    if(b > a and A >= x):
        x += A - x
    n -= 1
print(x)