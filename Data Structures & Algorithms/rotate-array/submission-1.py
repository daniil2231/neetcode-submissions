class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start, count = 0, 0

        while count < n:
            curr = start
            save = nums[curr]
            while True:
                nextIdx = (curr + k) % n
                save, nums[nextIdx] = nums[nextIdx], save
                count += 1
                curr = nextIdx

                if curr == start:
                    break
            start += 1