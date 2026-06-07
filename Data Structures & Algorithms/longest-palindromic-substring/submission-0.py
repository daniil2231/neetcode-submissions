class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            return False

        res = ""
        for i in range(len(s)):
            for j in range(len(s) - 1, -1, -1):
                newS = s[i:j + 1]
                if isPalindrome(newS) and len(newS) > len(res):
                    res = newS
        return res
