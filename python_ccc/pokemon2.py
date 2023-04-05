k = int(input())  # Your Pokemon's power
n = int(input())  # Number of opponents

opponents = list(map(int, input().split()))  # List of opponents' powers

day = 0  # Keep track of number of days
i = 0  # Index of current opponent

while k > 0 and i < n:
    day += 1
    battles_left = n - i  # Number of opponents left to battle
    rest_days = (battles_left - 1) // 2  # Number of days needed to rest

    # Battle as many opponents as possible in one day
    while i < n and k > 0:
        if k >= opponents[i]:
            k -= opponents[i]
            i += 1
        else:
            break

    # Rest for required number of days
    k = min(k + rest_days, 1000)

# Output result
if i == n:
    print(day)
else:
    print(-1)