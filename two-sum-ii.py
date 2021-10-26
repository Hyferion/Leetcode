def twoSum(numbers, target):
    table = {}
    for index, x in enumerate(numbers):
        if (target - x) in table:
            return [table[target - x], index + 1]
        else:
            table[x] = index + 1