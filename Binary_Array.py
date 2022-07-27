n=int(input())
s=list(map(int,input().split()))
c=0
for i in range(n):
    if s[i]==0 or s[i]==1:
        c+=1
    else:
        c=0
        break
if c==0:
    print("False")
else:
    print("True")