class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l,r=0, len(s)-1
        
        while l<r:
            if s[l]!=s[r]:
                includes_right,includes_left=s[l:r],s[l+1:r+1]
                return includes_right==includes_right[::-1] or includes_left==includes_left[::-1]
            l+=1
            r-=1
        return True
