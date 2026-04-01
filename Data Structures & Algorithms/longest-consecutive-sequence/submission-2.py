class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)

        count = 0
        max_count = 0
        for num in nums:
            count = 0
            if num in s:
                temp = num
                while temp in s:
                    count += 1
                    temp -= 1
                temp = num + 1
                while temp in s:
                    count += 1
                    temp += 1

                max_count = max(count, max_count)
        
        return max_count