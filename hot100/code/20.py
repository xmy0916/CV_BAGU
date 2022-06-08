class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        for i in s:
            if len(res) == 0:
                res.append(i)
            else:
                if self.is_match(res[-1],i):
                    res.pop()
                else:
                    if i in "])}":
                        return False
                    else:
                        res.append(i)
        if len(res) == 0:
            return True
        else:
            return False


    def is_match(self,left,right):
        if left == "(" and right == ")":
            return True
        elif left == "{" and right == "}":
            return True
        elif left == "[" and right == "]":
            return True
        return False