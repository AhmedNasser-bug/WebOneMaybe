l = input().split(" ")
m = [int(i) for i in l]
o = 0
for x in m:
    if(x  in m[m.index(x)+1: ]):
        o  += 1
    else:
        o -= 1
print(o)