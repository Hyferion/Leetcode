from random import shuffle


def quick_sort(arr, start, end):
    if len(arr) == 1:
        return arr
    if start < end:
        pi = partition(arr, start, end)

        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)
    return arr


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [2, 3, 6, 7, 1, 4]
print(quick_sort(arr, 0, len(arr) - 1))
print(1//2)