n=int(input())
s=list(map(int,input().split()))
k=set(s)
k=list(k)
c=0
for i in k:
    if(i==s.count(i)):
        c+=1
print(c)
    