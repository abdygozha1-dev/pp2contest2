n=int(input())
a=list(map(int, input().split()))
a.sort()
for i in range(len(a)-1, -1, -1):
    print(a[i], end=' ')