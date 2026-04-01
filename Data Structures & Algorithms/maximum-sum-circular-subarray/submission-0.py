class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sum = 0
        curr_max = 0
        global_max = nums[0]
        curr_min = 0
        global_min = nums[0]

        for num in nums:
            curr_max = max(curr_max + num, num)
            global_max = max(curr_max, global_max)

            curr_min = min(curr_min + num, num)
            global_min = min(global_min, curr_min)

            sum += num

        if global_max < 0:
            return global_max

        return max(sum - global_min, global_max) 

        # ln = len(nums)
        # max_so_far = nums[0]
        # for i in range(ln):
        #     max_so_far = max(self.kadanes(nums[i:] + nums[:i]), max_so_far)
        
        # return max_so_far


    def kadanes(self, nums: List[int]) -> int:
        global_max = nums[0]
        curr = 0

        for num in nums:
            curr = max(num, curr + num)
            global_max = max(curr, global_max)

        return global_max