class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        
        i = 0
        for idx in range(len(counts)):
            for _ in range(counts[idx]):
                nums[i] = idx
                i += 1
        