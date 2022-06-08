class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums = [5, 7, 7, 8, 8, 10]
        length = len(nums)
        if length == 0:
            return [-1,-1]
        left, right = 0, length - 1
        while left <= right:
            mid = int((left + right)/2)
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left < 0 or left >= length or nums[left] != target:
            left_bound = -1
        else:
            left_bound = left
        left, right = 0, length - 1
        while left <= right:
            mid = int((left + right)/2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if right >= length or right < 0 or nums[right] != target:
            right_bound = -1
        else:
            right_bound = right

        return [left_bound,right_bound]