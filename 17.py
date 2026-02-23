n=int(input())
a=[]
for i in range(n):
    s=input()
    a.append(s)
b=set(a)
cnt=0
for x in b:
    if a.count(x)==3: cnt+=1
print(cnt)