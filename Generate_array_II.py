n = int(input())
l = list(map(int,input().split()))
l1 ,l2 = [],[]
for i in range(len(l)):
    if(i%2 == 1):
        l1.append(l[i])
    else:
        l2.append(l[i])
for i in range(len(l2)):
    o = l1[i]
    for j in range(o):
        print(l2[i] ,end =" ")