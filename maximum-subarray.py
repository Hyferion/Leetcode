def maxSubArray(nums) -> int:
    windowSum = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        windowSum = max(windowSum + nums[i], nums[i])
        maxSum = max(windowSum, maxSum)
    return maxSum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
