n=int(input())
s=list(map(int,input().split()))
k=set(s)
k=list(k)
x=[]
for i in k:
    if(i==s.count(i)):
        x.append(i)
if(len(x)> 0):
    x.sort()
    print(x[0],x[-1])
else:
    print(-1)