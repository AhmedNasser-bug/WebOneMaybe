n , t = map(int , input().split(" "))
s = input()
r = list(s)
ln = False
for l in range(t):
    b = s.count("B")
    i = 0
    while(i < n - 1 ):
            if(ln):
                ln = False
                i += 1
                continue
            if(r[i] == "B" and  r[i + 1] == "G" ):    
                r[i]  = "G"
                r[i + 1] = "B"
                if(i != n - 2):
                    ln = True
            i += 1
print("".join(r))