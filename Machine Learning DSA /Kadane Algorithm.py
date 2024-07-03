def max_subarray(arr):
  max_so_far = arr[0]
  max_end = arr[0]
  
  for i in range(1, len(arr)):
    max_end = max(arr[i], max_end +arr[i])
    max_so_far = max(max_so_far, max_end)

return max_so_far

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(arr))
