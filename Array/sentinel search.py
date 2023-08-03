def sentinelSearch(arr, key):
    last = arr[len(arr) - 1]
    arr[len(arr) - 1] = key
    i = 0
    while arr[i] != key:
        i += 1
    arr[len(arr) - 1] = last
    if i < len(arr) - 1 or last == key:
        return i
    else:
        return -1
 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = 5

if sentinelSearch(arr,key):
    print("found")
else:
    print("not found")

