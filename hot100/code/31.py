class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length):
            reversed_i = length - i - 1
            if nums[reversed_i] > nums[reversed_i-1]:
                nums[reversed_i:] = sorted(nums[reversed_i:])
            for j in range(reversed_i, length):
                if nums[j] > nums[reversed_i-1]:
                    nums[j], nums[reversed_i-1] = nums[reversed_i-1], nums[j]
                    return
        # 这是第一个答案
        sorted(nums)