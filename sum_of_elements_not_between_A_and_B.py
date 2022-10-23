n = int(input())
l = list(map(int,input().split()))
a,b = map(int,input().split())
l.sort()
k1 ,k2 = 0,0
for i in range(len(l)):
    if(l[i] <= a):
        k1 = i
    if(l[i] <= b):
        k2 = i
c =[]        
for i in range(k1,k2+1):
    c.append(l[i])
print(abs(sum(c)- sum(l)))