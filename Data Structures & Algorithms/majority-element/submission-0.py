class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, count = 0, 0
        
        for n in nums:
            if count == 0:
                maj = n
                count += 1
            elif n == maj:
                count += 1
            else:
                count -= 1
        
        return maj