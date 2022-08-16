n=int(input())
c=1
for i in range(2,(n//2)+1):
    if n%i==0:
        c+=i
if c==n:
    print("True")
else:
    print("False")