class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sendBack = 0
        k = len(nums)

        for i in range(len(nums)):
            if nums[i] == val:
                sendBack += 1
                k -= 1
            else:
                nums[i - sendBack] = nums[i]

        return k