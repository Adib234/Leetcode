class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            if exponent % 2 == 0:
                return function(base*base, exponent//2)
            else:
                return base*function(base*base, (exponent-1)//2)

        f = function()

        return float(f) if n >= 0 else 1/f
