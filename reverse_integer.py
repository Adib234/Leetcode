class Solution:
    def reverse(self, x: int) -> int:

        negative = False
        if (x < 0):
            negative = True
            x *= -1
        reverse = 0
        while x > 0:
            reverse = (reverse*10)+(x % 10)
            x = x//10
        if 2**31-1 <= reverse or reverse <= -2**31:
            return 0
        return reverse*-1 if negative else reverse
