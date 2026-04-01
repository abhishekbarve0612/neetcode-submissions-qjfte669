class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = { nums[0]: 1}
        minimum = nums[0]

        for num in nums[1:]:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1

            if hash[num] > hash[minimum]:
                minimum = num
            if hash[minimum] > len(nums) // 2:
                return minimum
        return nums[0]