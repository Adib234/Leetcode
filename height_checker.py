class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = sorted(heights)
        diff = 0
        for i in range(len(a)):
            if a[i] != heights[i]:
                diff += 1
        return diff
