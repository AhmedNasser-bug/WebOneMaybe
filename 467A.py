n = int(input())
x = 0
for i in range(n):
    p, q = map(int, input().split(" "))
    if(p < q-1):
        x += 1
print(x)