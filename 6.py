n=int(input())
a=list(map(int, input().split()))
maxi=a[0]
for x in a:
    if x>maxi: maxi=x
print(maxi)