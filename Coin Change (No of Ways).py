coins = [3,5]
n = 5
coinWays = [0 for j in range(n+1)]
coinWays[0] = 1

for i in range(len(coins)):
  for j in range(n+1):
    if j>=coins[i]:
      coinWays[j] += coinWays[j-coins[i]]
print coinWays
