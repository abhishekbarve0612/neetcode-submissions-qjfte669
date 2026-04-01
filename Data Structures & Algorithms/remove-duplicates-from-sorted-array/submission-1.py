class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dix = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[dix] = nums[i]
                dix += 1
        return dix
        