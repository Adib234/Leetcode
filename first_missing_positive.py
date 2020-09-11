class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr = 1
        for i in nums:
            if i > curr:
                curr = i+1
        return curr
