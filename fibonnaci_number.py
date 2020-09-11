class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

#         if N==0:
#             return 0

#         a,b=0,1
#         temp=0
#         for i in range(N-1):
#             temp=b
#             b=a+b
#             a=temp
#         return b

        cache = {0: 0, 1: 1}
        if N == 1 or N == 0:
            return cache[N]

        for i in range(N-1):
            cache[i+2] = cache[i]+cache[i+1]
        return cache[N]
