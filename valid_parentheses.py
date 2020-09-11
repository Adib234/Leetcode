class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        dict_check = {"}": "{", ")": "(", "]": "["}
        for char in s:

            if char in dict_check:
                top = stack.pop() if stack else '#'

                if top != dict_check[char]:
                    return False

            else:
                stack.append(char)

        return not stack
