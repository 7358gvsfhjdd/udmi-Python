arr = [10, 20, 30, 40, 50]
key = 40

low, high = 0, len(arr)-1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Found at index", mid)
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
