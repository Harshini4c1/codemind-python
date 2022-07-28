n=int(input())
l=list(map(int,input().split()))
k=set(l)
c=0
for i in k:
    if i%2==1:
        c+=1
print(c)