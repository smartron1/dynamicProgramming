coins = [3,5,6]
n = 11
coinsDP = [9999999 for i in range(n+1)]
coinsDP[0] = 0

for i in range(len(coins)):
  for j in range(1, n+1):
    if j >= coins[i]:
      coinsDP[j] = min(coinsDP[j], coinsDP[j - coins[i]]+1)



print str(coinsDP)
ans = 0

print "Minimum Number of Coins Required To Make %s are %s"%(n,coinsDP[-1])
