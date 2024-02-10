inl = input().split(' ')
k = int(inl[0])
n = int(inl[1])
w = int(inl[2])
b = 0
i = 1
while(w > 0):
    b += i*k
    w -= 1
    i += 1
if(n > b):
    print(0)
else:
    print(b - n)
