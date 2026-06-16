class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        shift = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                k -= 1
                shift += 1
            else:
                nums[i - shift] = nums[i]
        
        return k