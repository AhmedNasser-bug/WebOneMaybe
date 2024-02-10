x = int(input())
m =0 
r=  0
while(x  %  5  !=  0 ):
        r += 1
        x -= 1
m    +=  x/ 5
for  i  in range(4 , 0  , -1):
    if(r % i == 0):
        m += r/i
        break
print(int(m))