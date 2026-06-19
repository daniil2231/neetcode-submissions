class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {x: 0 for x in nums}

        for n in nums:
            freq[n] += 1
        
        return [x for x in freq.keys() if freq[x] > math.floor(len(nums) / 3)]