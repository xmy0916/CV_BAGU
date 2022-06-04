class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for index, n in enumerate(nums):
            my_dict[n] = index

        for res1, n in enumerate(nums):
            res2 = my_dict.get(target - n)
            if res2 and res2 != res1:
                return [res1, res2]

        return None