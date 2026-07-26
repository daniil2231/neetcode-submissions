class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(curr, seen):
            if len(curr) == len(nums):
                res.append(curr)
                return
            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    seenc = seen.copy()
                    seenc.add(nums[i])
                    currc = curr.copy()
                    currc.append(nums[i])
                    bt(currc, seenc)
        
        bt([], set())
        return res