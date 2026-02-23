n=int(input())
a=list(map(int, input().split()))
b=[]
for x in a:
    if x not in b:
        print("YES")
        b.append(x)
    else:
        print("NO")