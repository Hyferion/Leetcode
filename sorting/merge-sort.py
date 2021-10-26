def merge_sort(numbers):
    list_length = len(numbers)

    if list_length <= 1:
        return numbers

    mid_point = list_length // 2

    left_partition = merge_sort(numbers[:mid_point])
    right_partition = merge_sort(numbers[mid_point:])

    return merge(left_partition, right_partition)


def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output


def run_merge_sort():
    unsorted_list = [4, 1, 5, 7, 2, 6]
    print(unsorted_list)
    print(merge_sort(unsorted_list))


run_merge_sort()
