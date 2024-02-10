Fir = input().split(" ")
n = int(Fir[0])
h = int(Fir[1])
sec = input().split(" ")
i = 0
r =0
for i in sec:
    if(int(i) <= h ):
        r+= 1
    if(int(i) > h):
        r += 2
print(r)