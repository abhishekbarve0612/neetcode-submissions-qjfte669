class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        uniques = set()

        sz = len(nums)

        for i in range(sz):
            for j in range(i + 1, sz):
                current_sum = nums[i] + nums[j]
                targetSumMatch = self.twoSum(nums[i + 1:j] + nums[j + 1: sz], target - current_sum)

                for match in targetSumMatch:
                    uniques.add(tuple(sorted([nums[i], nums[j], match[0], match[1]])))

        return [list(tpl) for tpl in uniques]

    def twoSum(self, nums: List[int], target: int):
        hash = {}
        result = []
        fp, sp = 0, len(nums) - 1

        while fp < sp:
            sm = nums[fp] + nums[sp]

            if sm == target:
                result.append([nums[fp], nums[sp]])
                fp += 1
                sp -= 1

            elif sm > target:
                sp -= 1
            else:
                fp += 1

        return result