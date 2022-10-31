a, b = map(int,input().split())
l = list(map(int,input().split()))
k = list(map(int,input().split()))
j = l+k
j = set(j)
count = 0
for i in j:
    if(l.count(i)>0 and k.count(i)>0 ):
        count+=1
print(count)        