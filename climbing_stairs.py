class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        bottom_up = [i for i in range(n)]

        bottom_up[0], bottom_up[1] = 1, 2

        for i in range(2, n):
            bottom_up[i] = bottom_up[i-1]+bottom_up[i-2]

        return bottom_up[-1]
