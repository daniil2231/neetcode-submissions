class Solution:
    def validPalindrome(self, s: str) -> bool:        
        def isPalindrome(inp):
            return inp == inp[::-1]

        for i in range(len(s)):
            if isPalindrome(s[:i] + s[i + 1:]):
                return True
        return False
