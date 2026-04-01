class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(list(s)) != len(nums)