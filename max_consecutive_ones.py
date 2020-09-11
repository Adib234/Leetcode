class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = []
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            if nums[i] != 1:
                maxi.append(temp)
                temp = 0
        maxi.append(temp)
        return max(maxi)
