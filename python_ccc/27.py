import math
# lis = list(map(int,input().split(" ")))
# def fact(num):
#     if(math.factorial(num)== num):
#         return num
#     else: 
#         def filterfact(n):
#             for i in range(2,lis):
#                 ref /=i
#                 if (ref ==1):
#                     return True
# print(list(map))
def filterfact(ref):
            for i in range(2,ref):
                ref /=i
                if (ref ==1):
                    return True

ref = list(map(int,input().split(" ")))
def mapper(ref):
       for i in range(2,ref):
              ref/=i
              if(ref==1):
                     return i

print(list(map(mapper,list(filter(filterfact,ref)))))