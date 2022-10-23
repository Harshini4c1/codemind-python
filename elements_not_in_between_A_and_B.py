n = int(input())
l = list(map(int,input().split()))
a,b = map(int,input().split())
j = l.copy()
k1,k2=0,0
l.sort()
for i in range(len(l)):
    if(l[i] <= a):
        k1 = i
    if(l[i] <= b):
        k2 = i
c =[]        
for i in range(k1,k2+1):
    c.append(l[i])
k =[]
for i in j:
    if(i not in c):
        k.append(i)
if(len(k)>0):
    print(*k)
else:
    print(-1)