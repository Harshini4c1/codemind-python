n=int(input())
s=list(map(int,input().split()))
k=[]
for i in s:
    if(i not in k):
        k.append(i)
print(*k)
    