class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergeSort(low, high):
            if low >= high:
                return

            mid = (high + low) // 2

            mergeSort(low, mid)
            mergeSort(mid + 1, high)
            merge(low, mid, high)

        def merge(low, mid, high):
            temp = []
            i, j = low, mid + 1

            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                
                if nums[j] < nums[i]:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= high:
                temp.append(nums[j])
                j += 1
            
            for i in range(0, len(temp)):
                nums[i + low] = temp[i]
        
        mergeSort(0, len(nums) - 1)
        return nums