class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1

        while count < len(nums):
            nums[count] = 0
            count += 1


solution = Solution()
solution.moveZeroes([0, 0, 1])
