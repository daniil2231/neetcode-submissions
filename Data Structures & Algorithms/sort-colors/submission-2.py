class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {0: 0, 1: 0, 2: 0}
        for n in nums:
            freq[n] += 1

        curr = 0
        for i in range(len(nums)):
            while freq[curr] == 0:
                curr += 1
            nums[i] = curr
            freq[curr] -= 1