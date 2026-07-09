class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set()
        for num in nums:
            s.add(num)
        
        longest = 1
        for el in s:
            if (el - 1) not in s:
                x = count = 1
                while (el + x) in s:
                    count += 1
                    longest = max(longest , count)
                    x += 1
            
        return longest