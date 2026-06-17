class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            if needle == haystack[i:i + len(needle)]:
                return i
            i += 1
        return -1