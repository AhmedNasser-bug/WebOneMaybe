inp = input().split(' ')
n = int(inp[0])
k = int(inp[1])
for i in range(k , 0 , -1):
    l = str(n)[-1]
    if(l != '0'):
        n -= 1
    else:
        n = int(n /10)
print(n)