n = int(input())
while(True):
    n += 1
    l = str(n)
    if(l[0] not in l[1: 4] and l[1] not in l[2 : 4] and l[2] not in l[3:4] and l[3] not in l[:3]):
        print(n)
        break