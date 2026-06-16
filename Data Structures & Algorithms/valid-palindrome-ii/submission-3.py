class Solution:
    def validPalindrome(self, s: str) -> bool:        
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipLeft = s[l + 1:r + 1]
                skipRight = s[l:r]
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
            else:
                l += 1
                r -= 1

        return True