class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        s = 0
        res = 0
        for n in nums:
            s += n
            if s == k:
                res += 1
            
            res += sums[s - k]
            sums[s] += 1
        return res