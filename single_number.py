class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        right = len(nums)-1
        left = 0
        occurences = {}
        while right >= left:

            if nums[left] not in occurences.keys():
                occurences[nums[left]] = 1
                left += 1
            else:
                occurences[nums[left]] += 1
                left += 1
            if left >= right:
                break
            if nums[right] not in occurences.keys():
                occurences[nums[right]] = 1
                right -= 1
            else:
                occurences[nums[right]] += 1
                right -= 1
        if len(nums) == 1:
            occurences[nums[0]] = 1

        for i in occurences.keys():
            if occurences[i] == 1:
                return i
