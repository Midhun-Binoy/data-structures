def selection_sort(arr):
  for i in range(len(arr) - 1):
    minidx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[minidx]:
        minidx = j
    arr[i], arr[minidx] = arr[minidx], arr[i]

arr = [4, 3, 2, 1, 0]
selection_sort(arr)
print(arr)