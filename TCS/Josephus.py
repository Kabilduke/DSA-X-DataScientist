def circle(n, k):
  index = 0
  for i in range(k, n+1):
    index = (index+k)%i
  return index+1


n = 5
k = 2
print(circle(n, k))
  
