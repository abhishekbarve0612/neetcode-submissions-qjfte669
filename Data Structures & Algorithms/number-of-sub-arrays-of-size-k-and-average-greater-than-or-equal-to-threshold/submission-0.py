class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        length = len(nums)

        running_sum = sum(nums[:k])

        count = 0

        if running_sum // k >= threshold:
            count += 1

        L = k - 1

        for R in range(k, length):
            running_sum += nums[R]
            running_sum -= nums[R - k]
            if running_sum // k >= threshold:
                count += 1
            L += 1

        return count