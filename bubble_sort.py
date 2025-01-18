<<<<<<< HEAD
def bubble_sort(arr):
  for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [4, 3, 2, 1, 0]
bubble_sort(arr)
=======
def bubble_sort(arr):
  for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [4, 3, 2, 1, 0]
bubble_sort(arr)
>>>>>>> a182fa2465f881014a46d8d73e3d827a6ed8ec40
print(arr)