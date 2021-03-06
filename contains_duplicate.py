class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        for i in nums:
            if i in duplicate:
                return True
            else:
                duplicate.add(i)
        return False
