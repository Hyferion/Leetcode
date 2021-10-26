array = [3, 2, 1, 6, 4, 9, 8, 7, 5, 0]


def insertion_sort(arr):
    for slot in range(1, len(arr)):
        print(slot)
        value = arr[slot]
        prev_slot = slot - 1

        while prev_slot > -1 and arr[prev_slot] > value:
            arr[prev_slot + 1] = arr[prev_slot]
            print(arr)
            prev_slot = prev_slot - 1
        arr[prev_slot + 1] = value
    return arr

insertion_sort(array)