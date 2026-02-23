n=int(input())
a=list(map(int, input().split()))
maxi=a[0]
for x in a:
    if x>maxi: maxi=x
mini=a[0]
for x in a:
    if x<mini: mini=x
for i in range(len(a)):
    if a[i]==maxi: a[i]=mini
for x in a:
    print(x, end=' ')