class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        first, second = 0, 0

        minm = 2 ** 32

        csum = 0

        while second < len(nums):
            csum += nums[second]

            while csum >= target:
                minm = min(second - first + 1, minm)

                csum -= nums[first]
                first += 1
            second += 1

        return minm if minm != 2 ** 32 else 0
