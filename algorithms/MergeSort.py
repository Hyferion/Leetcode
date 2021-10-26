array = [3, 4, 2, 6, 1, 9, 8, 7, 5, 0]


def merge_sort(array):
    if len(array) <= 1:
        return array

    array1 = array[:len(array) // 2]
    array2 = array[len(array) // 2:]
    print(array1)
    print(array2)

    array1 = merge_sort(array1)
    array2 = merge_sort(array2)

    return merge(array1, array2)


def merge(array1, array2):
    result = []
    print("Merge: " + str(array1) + ":" + str(array2))

    while len(array1) > 0 and len(array2) > 0:
        if array1[0] > array2[0]:
            result.append(array2[0])
            del array2[0]

        else:
            result.append(array1[0])
            del array1[0]

    while len(array1) > 0:
        result.append(array1[0])
        del array1[0]

    while len(array2) > 0:
        result.append(array2[0])
        del array2[0]

    print("Result: " + str(result))
    return result


sorted_array = merge_sort(array)
print(sorted_array)
