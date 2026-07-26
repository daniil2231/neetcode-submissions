class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(curr, seen):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    curr.append(nums[i])
                    bt(curr, seen)
                    seen.remove(nums[i])
                    curr.pop()
        
        bt([], set())
        return res