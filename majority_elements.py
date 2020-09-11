class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        checks = {}
        left = 0
        right = len(nums)-1
        while right >= left:
            if nums[left] not in checks.keys():
                checks[nums[left]] = 1
                left += 1
            else:
                checks[nums[left]] += 1
                left += 1
            if nums[right] not in checks.keys():
                checks[nums[right]] = 1
                right -= 1
            else:
                checks[nums[right]] += 1
                right -= 1
        if len(nums) == 1:
            return nums[0]
        for i in checks.keys():
            if checks[i] > majority:
                return i
        #counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
