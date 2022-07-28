n=int(input())
s=list(map(int,input().split()))
s1=int(input())
k=set(s)
k=list(k)
d=[]
for i in k:
    if(s1==s.count(i)):
        d.append(i)
if len(d)!=0:
    print(*d)
else:
    print(-1)