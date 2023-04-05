lis = [3,15,4,27]
n= int(input())
for i in range(0,n):
    x = int(input())
    if x%2==0:
        lis.insert(0,x)
    else:
        lis.append(x)
print(lis)