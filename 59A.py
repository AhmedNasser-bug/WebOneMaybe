s = input()
u = 0
l =0
for i in s:
    if(i.islower()):
        l += 1
    else:
        u += 1
if(u > l):
    print(s.upper())
elif(u < l or u == l):
    print(s.lower())