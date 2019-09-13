gold = [[1, 3, 1, 5], 
    [2, 2, 4, 1], 
    [5, 0, 2, 3], 
    [0, 6, 1, 2]] 
  
m = 4
n = 4

goldDP = [[0 for i in range(m)] for j in range(n)]
for col in range(n-1,-1,-1):
  for row in range(n):
    if col == n-1:
      right = 0
    else:
      right = goldDP[row][col+1]
    if row == 0 or col == n-1:
      rightUp = 0
    else:
      rightUp = goldDP[row-1][col+1]
    if row == m-1 or col == n-1:
      rightDown = 0
    else:
      rightDown = goldDP[row+1][col+1]
    goldDP[row][col] = gold[row][col] + max(right, rightUp, rightDown)
ans = 0
for i in goldDP:
  ans = max(ans, max(i))
print ans
