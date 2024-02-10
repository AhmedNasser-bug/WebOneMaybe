x = input()
y = input()
l = list()
i = 0
while i < len(x):
    if(x[i] == y[i]):
        l.append("0")
    else:
        l.append("1")
    i +=1
print("".join(l))