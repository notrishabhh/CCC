#ref = "python"
#n = int(input())
#print(ref[-n:]+ref[:-n])
#print(ref[:-n],end="")


st = input()
n = int(input())
print(st[len(st)-n:]+st[:len(st)-n])