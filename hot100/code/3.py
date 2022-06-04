class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {}
        start, end = 0, 0
        length = 0
        for index, c in enumerate(s):
            if c not in my_dict.keys():
                my_dict[c] = index
                length = max(length, index - start + 1)
            else:
                start = max(start, my_dict[c] + 1)
                length = max(length, index - start + 1)
                my_dict[c] = index
        return length