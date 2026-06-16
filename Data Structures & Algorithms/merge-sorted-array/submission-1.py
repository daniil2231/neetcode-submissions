class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        n1 = nums1[:m + 1]

        for i in range(m + n):
            if r >= n:
                nums1[i] = n1[l]
                l += 1
            elif l >= m:
                nums1[i] = nums2[r]
                r += 1
            else:
                if n1[l] <= nums2[r]:
                    nums1[i] = n1[l]
                    l += 1
                else:
                    nums1[i] = nums2[r]
                    r += 1