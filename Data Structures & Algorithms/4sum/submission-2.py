class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # -1 -1 -1 1 1 1
        if len(nums) < 4:
            return []

        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r] 
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        res.add(tuple([nums[i], nums[j], nums[l], nums[r]]))
                        r -= 1
        return list(res)