class Solution:
    def findKthLargest(self, nums, k):
        target_index = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1, target_index)

    def quickSelect(self, arr, low, high, target_index):
        pivotIndex = self.partition(arr, low, high)
        
        if pivotIndex == target_index:
            return arr[pivotIndex]
        elif pivotIndex < target_index:
            return self.quickSelect(arr, pivotIndex + 1, high, target_index)
        else:
            return self.quickSelect(arr, low, pivotIndex - 1, target_index)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while i <= high and arr[i] <= pivot:
                i += 1
            while j >= low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j