# Linear search
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i+1
  return -1

arr = [1, 2, 3, 4, 5]
target = 2
print(linear_search(arr, target))