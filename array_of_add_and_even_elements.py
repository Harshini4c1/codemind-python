n = int(input())
l =list(map(int,input().split()))
l1 ,l2 =[], []
for i in l:
    if(i%2 == 1):
        l1.append(i)
    else:
        l2.append(i)
k = l1+l2
print(*k)