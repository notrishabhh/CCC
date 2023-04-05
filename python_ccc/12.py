teams = []
for i in range(int(input("number of elem:"))):
    teams.append(input("elements"))
for i in range(len(teams)):
    for j in range (i+1,len(teams)):
        print(f'{teams[i]} vs {teams[j]}' )