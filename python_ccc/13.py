import math
x = []
for i in range(int(input("Number of elements:"))):
    x.append(input("elements"))
if x[i]%2==0:
    print(i**2)
else:
    print(math.factorial(i))

#n = list(map(int(input().split(" "))))
#n = sum(list(map(int(input().split("")))))

def ert(num):
    print(num%2==0)