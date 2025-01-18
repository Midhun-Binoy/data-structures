<<<<<<< HEAD
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i+1
  return -1

arr = [1, 2, 3, 4, 5]
target = 2
=======
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i+1
  return -1

arr = [1, 2, 3, 4, 5]
target = 2
>>>>>>> a182fa2465f881014a46d8d73e3d827a6ed8ec40
print(linear_search(arr, target))