class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        max_lan = 0
        max_index = 0
        tmp_len = 1

        for i in range(length):
            # 去重，连续中心就找一次就好了
            if i >= 1 and s[i] == s[i - 1]:
                continue
            left = i - 1
            right = i + 1

            # 找到当前中心往左一直一样的连续中心
            while left > 0 and s[left] == s[i]:
                tmp_len += 1
                left -= 1

            # 找到当前中心往右一直一样的连续中心
            while right < length and s[right] == s[i]:
                tmp_len += 1
                right += 1

            while left >= 0 and right < length and s[left] == s[right]:
                tmp_len += 2
                left -= 1
                right += 1

            if tmp_len > max_lan:
                max_lan = tmp_len
                max_index = left
            tmp_len = 1

        return s[max_index + 1:max_index + max_lan + 1]
