# lis = (list(map(str,input().split(" "))))
# lis2 = []
# vow = "aeiouAEIOU"
# for i in (lis):
#     for j in vow:
#         if  j in i and i not in lis2:
#             lis2.append(i) 
# print(lis2)


lis= list(map(str,input().split(" ")))
def filtervow(num):
    count = 0
    vow = "aeiou"
    for i in vow:
        if i in num:
            count+=1
    if(count>0):
        return True
print(list(filter(filtervow,lis)))

