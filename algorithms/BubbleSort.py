array = [3, 2, 1, 6, 4, 9, 8, 7, 5, 0]


def bubble_sort(arr):
    for passnum in range(len(arr) - 1, 0, -1):
        print(passnum)
        for i in range(passnum):
            print(i)
            if arr[i] > arr[i + 1]:
                value = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = value


bubble_sort(array)
