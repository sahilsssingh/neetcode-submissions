class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        left_partition_len = (n1 + n2 + 1) // 2
        
        low, high = 0, n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left_partition_len - mid1

            left1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            left2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            right1 = nums1[mid1] if mid1 < n1 else float('inf')
            right2 = nums2[mid2] if mid2 < n2 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        