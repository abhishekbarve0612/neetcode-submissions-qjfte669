class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for idx, num in enumerate(nums):
            if leftSum == total - leftSum - num:
                return idx
            leftSum += num
        return -1