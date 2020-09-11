class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height)-1
        width = len(height)-1
        maximum = 0
        while width != 0:
            if height[a] >= height[b]:
                if width*height[b] >= maximum:
                    maximum = height[b]*width
                width -= 1
                b -= 1
            else:
                if width*height[a] >= maximum:
                    maximum = width*height[a]
                width -= 1
                a += 1
        return maximum
