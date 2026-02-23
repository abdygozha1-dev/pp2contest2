n=int(input())
a=list(map(int, input().split()))
e=set(a) #removes duplicates, but doesn't sort 2 1 3 4
b=sorted(e) #1 2 3 4
c=[] #әр елемент неше рет кездеседі
d=[] #сол элементтер
for x in b:
    cnt=0
    for y in a:
        if x==y: cnt+=1
    c.append(cnt)
    d.append(x)
max_cnt=c[0]
for x in c:
    if x>max_cnt: max_cnt=x
for i in range(len(c)):
    if max_cnt==c[i]: 
        print(d[i]) #as 1st element is min
        break