n = int(input())
for i in range(n):
    a =input()
    if (a.isalpha()):
            print(f'Hello {a}')
    elif (a.isnumeric()):
            print(f'{23+int(a)}')
    else:
            print("exit")

# a = "java"
# print(f'Hello python and {a}')