class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fp, sp = 0, 1

        while sp < len(nums):
            while sp < len(nums) and nums[fp] == nums[sp]:
                sp += 1

            if sp < len(nums):
                nums[fp + 1], nums[sp] = nums[sp], nums[fp + 1]
                fp += 1
            sp += 1

        return fp + 1