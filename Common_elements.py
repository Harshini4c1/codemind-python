a, b = map(int,input().split())
l = list(map(int,input().split()))
k = list(map(int,input().split()))
j = l+k
j = set(j)
c =[]
for i in l:
    if(k.count(i)>0 ):
        c.append(i)
o =[]
for i in c:
    if(i not in o):
        o.append(i)
print(*o)        
