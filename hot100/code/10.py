class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)

        dp = [[False]*(len_p+1) for i in range(len_s+1)]
        dp[0][0] = True

        for i in range(len_s+1):
            for j in range(1, len_p+1):
                if p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    case1 = dp[i][j-2] # *号前一个字符不用了
                    case2 = dp[i-1][j] if s[i-1] == p[j-2] or p[j-2] == '.' else False # *号前一个字符必须用
                    dp[i][j] = case1 | case2
                else:
                    if p[j-1] == s[i-1]:
                        dp[i][j] = dp[i-1][j-1]
        return dp[len_s][len_p]