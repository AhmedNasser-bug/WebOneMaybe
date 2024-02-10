x1  =  input()
x2 = input()
x = 0
A = "abcdefghijklmopqrstuvwxyz"
for x4 in x2:
    for x3 in x1:
        if(A.index(x3.lower()) < A.index(x4.lower())):
            x = -1
            break
        elif(A.index(x3.lower()) > A.index(x4.lower())):
            x = 1
            break
        else:
            x = 0
            break
print(x)