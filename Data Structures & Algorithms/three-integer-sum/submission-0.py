class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        s = set()

        nums.sort()

        for i in range(len(nums)):
            compliment = -nums[i]
            matches = self.twoSum(nums, i, compliment)
            for match in matches:
                s.add(tuple(sorted([nums[i], nums[match[0]], nums[match[1]]])))


        return [list(s) for s in s]

    def twoSum(self, nums: List[int], ignoreIdx: int, target: int) -> List[List[int]]:
        result = []
        hash = {}
        for i in range(len(nums)):
            if i == ignoreIdx:
                continue
            if nums[i] in hash:
                # result.append([hash[num], num]
                result.append([hash[nums[i]], i])
            else:
                hash[target - nums[i]] = i

        return result