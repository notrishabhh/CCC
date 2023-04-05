d ={}
n = int(input())
for i in range(n):
    index = int(input("Enter the index:"))
    value = int(input("Enter the value:"))
    d[index] = value
print(f'{d} "unsorted"')
r = sorted(d)
print(r)
d2 = {}
for k in r:
      d2[k]= d[k]
print(d2)