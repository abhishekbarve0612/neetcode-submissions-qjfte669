class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = {}

        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        result = []
        for key, val in hash.items():
            if val > len(nums) // 3:
                result.append(key)
        return result