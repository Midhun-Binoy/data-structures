<<<<<<< HEAD
def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

arr = [4, 3, 2, 1, 0]
insertion_sort(arr)
=======
def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

arr = [4, 3, 2, 1, 0]
insertion_sort(arr)
>>>>>>> a182fa2465f881014a46d8d73e3d827a6ed8ec40
print(arr)