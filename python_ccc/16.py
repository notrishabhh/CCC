def filtering(num):
    if(num%2==0):
        return True
    
ref = [3,4,5,6]
print(list(filter(filtering,ref)))


