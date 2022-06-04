# 非最优解
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        index1 = 0
        index2 = 0

        len1 = len(nums1)
        len2 = len(nums2)

        nums3 = []
        while index1 < len1 and index2 < len2:
            if nums1[index1] >= nums2[index2]:
                nums3.append(nums2[index2])
                index2 += 1
            else:
                nums3.append(nums1[index1])
                index1 += 1
        while index1 < len1:
            nums3.append(nums1[index1])
            index1 += 1

        while index2 < len2:
            nums3.append(nums2[index2])
            index2 += 1

        if len(nums3) % 2 == 0:
            return 0.5 * nums3[int(len(nums3) / 2 - 1)] + 0.5 * nums3[int(len(nums3) / 2)]
        else:
            return nums3[int((len(nums3) + 1) / 2) - 1]