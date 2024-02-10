L = input().split(' ')
a = int(L[0])
b = int(L[1])
i = 0
while (a <= b):
    a *= 3
    b *= 2
    i += 1
print(i)