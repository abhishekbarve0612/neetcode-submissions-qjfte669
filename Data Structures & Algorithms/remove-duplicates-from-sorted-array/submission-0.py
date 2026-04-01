class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fp = 0
        sp = 1
        count = 0
        while sp < len(nums):
            if nums[fp] != nums[sp]:
                count += 1
                nums[fp + 1] = nums[sp]
                fp += 1
                sp += 1
            else:
                sp += 1
                

        return count + 1
        