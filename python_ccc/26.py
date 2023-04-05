lis = list(map(str,input().split(" ")))
def filtervowels(st):
    vowels="aeiou"
    count=0
    for i in vowels:
        if i in st.lower():
            count+=1
    if (count<0):
        return True
def mapping(string):
    string=string.lower()
    vowels="aeiou"
    ref=""
    for i in string:
        if i in vowels:
            ref+=i*(string.index(i)+1)
        else:
            ref+=1
    return ref
print(list(map(mapping,list(filter(filtervowels,lis)))))