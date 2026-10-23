class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = []
        summ = 0
        for num in nums:
            summ += num
            self.prefix.append(summ)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)