arr1 = [3,4,-1,0,6,2,3]

longestSub = [1 for i in range(len(arr1))]
for i in range(1,len(arr1)):
  for j in range(i):
    if arr1[j] < arr1[i]:
      longestSub[i] = max((longestSub[j]+1), (longestSub[i]))
print longestSub
