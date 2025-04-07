class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = 0, 0, 0
        while k < (m + n):
            if j >= n:
                k += 1
                i += 1

            elif i >= m:
                # move back
                nums1[k+1:] = nums1[k:-1]
                nums1[k] = nums2[j]
                j += 1
                k += 1
                
            elif nums1[k] <= nums2[j]:
                k += 1
                i += 1

            else:
                # move back
                nums1[k+1:] = nums1[k:-1]
                nums1[k] = nums2[j]
                j += 1
                k += 1
