from math import sqrt
def isprime(n):
    if(n==1 or n==0 ):
        return False
    for i in range(2,int(sqrt(n)+1)):
        if(n%i == 0):
            return False
    return True
n = int(input())
l = list(map(int,input().split()))
k = 0
c = 0
for i in l:
    if(isprime(i) == True):
        k+= i
        c+=1
op = k/c
print("%0.2f"%op)