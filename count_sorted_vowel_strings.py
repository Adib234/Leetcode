class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        dp = [[j for j in range (5,0,-1)] for i in range(n)]
        
        
        for k in range(1,n):
            
            for a in range(3,-1,-1):
                
                dp[k][a]=dp[k-1][a]+dp[k][a+1]
                
        return dp[n-1][0]
