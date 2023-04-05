import math
def fact(num):
    return math.factorial(num)

ref = [1,2,3,4,5]
refmapped = list(map(fact,ref))
print(refmapped)