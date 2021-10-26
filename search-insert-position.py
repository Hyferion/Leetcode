"""Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0"""


def searchInsert(nums, target):
    insert_index = None
    print(len(nums))
    for index, n in enumerate(nums):
        if n >= target:
            insert_index = index
            break
        elif len(nums) == index + 1:
            insert_index = index + 1
    return insert_index


def searchInsert_fast(nums, target):
    insert_index = None
    for n in range(len(nums)):
        if nums[n] >= target:
            insert_index = n
            break
        elif len(nums) == n + 1:
            insert_index = n + 1
    return insert_index
