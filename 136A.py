n = int(input())
l = list(input().split(" "))
list1 = []
for o in range(0 , n ) :
    print(l , list1)
    for u in l:
        list1.insert ( int(l[int(l[o])- 1]) , int(l[o]) )
    l.pop(l.index(l[o]))
    
print(l)
for k in l:
    print(k , end = " ")