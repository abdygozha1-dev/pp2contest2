n, l, r=map(int, input().split())
a=list(map(int, input().split()))
b=[]
for i in range(len(a)):
    if i>=l-1 and i<=r-1:
        b.append(a[i])
b.reverse() 
c=[]
j=0
for i in range(len(a)):
    if i>=l-1 and i<=r-1:
        c.append(b[j])
        j+=1
    else:
        c.append(a[i])
for x in c:
    print(x, end=' ')

'''
input: 5 2 5
       2 8 10 5 12
index: 1 2  3 4  5
b: 12 5 10 8
c: 2 12 5 10 8
'''