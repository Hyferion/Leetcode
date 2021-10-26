def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    nums_c = nums.copy()
    for i in range(len(nums)):
        print(nums_c)
        print(nums)
        if i + k < len(nums):
            nums[i + k] = nums_c[i]
        else:
            nums[k - 1] = nums_c[i]


rotate([1, 2, 3, 4, 5, 6, 7], 3)
