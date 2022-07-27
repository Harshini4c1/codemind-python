n=int(input())
s=list(map(int,input().split()))
s.reverse()
k=0
for i in range(n):
    x=2**i
    k+=s[i]*x
print(k)
