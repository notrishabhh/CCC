import math
def filterOdd(num):
    if(num%2!=0):
        return True
lis1 = list(map(int,input().split(" ")))
def fact(n):
    return math.factorial(n)
print(list(map(fact,(list(filter(filterOdd,lis1))))))



# import math
# def filterOdd(num):
#     if(num%2!=0):
#         return True

# ref = list(map(int,input().split(" ")))
# def fact(n):
#     return math.factorial(n)
# print(list(map(fact,(list(filter(filterOdd,ref))))))