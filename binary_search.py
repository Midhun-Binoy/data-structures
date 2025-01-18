<<<<<<< HEAD
def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid+1
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

arr = [1, 2, 3, 4, 5, 6]
target = 4
=======
def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid+1
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

arr = [1, 2, 3, 4, 5, 6]
target = 4
>>>>>>> a182fa2465f881014a46d8d73e3d827a6ed8ec40
print(binary_search(arr, target))