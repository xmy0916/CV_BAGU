class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.my_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.res = []
        self.dfs(digits, 0, len(digits), [])
        return self.res

    def dfs(self, digits, depth, max_depth, tmp_res):
        if depth >= max_depth:
            self.res.append("".join(tmp_res))
            return

        for c in self.my_dict[digits[depth]]:
            self.dfs(digits, depth + 1, max_depth, tmp_res + [c])