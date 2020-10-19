class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        
        nums = sorted(zip(ages,scores))
        dp = [0]*len(nums)
        
        for i in range (len(nums)):
            dp[i]=nums[i][1]
            
            for j in range (i):
                if nums[i][1]>=nums[j][1]:
                    dp[i]=max(dp[i],nums[i][1]+dp[j])
        
        return max(dp)
