class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        ph = ""
        while l < r:
            ph = s[l]
            s[l] = s[r]
            s[r] = ph
            l += 1
            r -= 1