n=int(input())
a=[] 
for i in range(n):
    s=input()
    a.append(s)
e=set(a) #removes duplicates, but not sorted, a,b,c..z
b=sorted(e) #sorted
c=[] #тура b жай келесі элемент бұрын болды ма соны тексеру үшін керемет
d=[] #стринг алғаш рет кіргендегі позиция сақтайды
for x in b:
    for i in range(len(a)):
        if x==a[i] and x not in c:
            c.append(x)
            d.append(i+1)
for i in range(len(c)):
    print(c[i], d[i])

'''
input: 3
ab
ab
cd
output: ab 1
cd 3
a= ['ab', 'ab', 'cd']
b=c= ['ab', 'cd']
d=[1, 3]
'''