n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
for i in range(n):
    if a<=s[i]>=b:
        d.append(s[i])
if len(d)==0:
    print(-1)
else:
    print(max(d))   
    