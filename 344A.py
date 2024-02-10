n = int(input())
l = list()
x = 0
i =0
for o in range(n):
    m= input()
    l.append(m)
while(i < n - 1):
    if(int(l[i][1]) == int(l[i+ 1][0])):
        x += 1
    i += 1
print(x+ 1)
