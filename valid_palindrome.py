class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string=''.join(i for i in s if i.isalnum()).lower()
        return new_string[::-1]==new_string
