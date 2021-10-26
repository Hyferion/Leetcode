def insertion_sort(numbers):
    for i in range(len(numbers)):
        for k in range(i, 0, -1):
            if numbers[k] < numbers[k - 1]:
                numbers[k - 1], numbers[k] = numbers[k], numbers[k - 1]
    return numbers


print(insertion_sort([2, 1, 5, 7, 3, 6, 2]))
