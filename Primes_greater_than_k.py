from math import sqrt
def isprime(n):
    if( n==1 or n ==0 ):
        return False
    for i in range(2, int(sqrt(n)+1)):
        if(n%i == 0):
            return False
    return True
n = int(input())
l = list(map(int,input().split()))
k = int(input())
count=0
for i in l:
    if(i>=k):
        if(isprime(i) == True):
            count +=1
print(count) 