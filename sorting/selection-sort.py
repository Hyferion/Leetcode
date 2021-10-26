def selection_sort(numbers):
    for k in range(len(numbers)):
        low_ind = k
        for i in range(k + 1, len(numbers)):
            if numbers[i] < numbers[low_ind]:
                low_ind = i

        numbers[k], numbers[low_ind] = numbers[low_ind], numbers[k]

    return numbers


print(selection_sort([9, 3, 6, 4, 7, 3, 3]))
