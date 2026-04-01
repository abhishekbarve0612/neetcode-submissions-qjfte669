class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1

        maxWater = 0

        while start < end:

            distance = end - start

            maxWater = max(
                min(heights[start], heights[end]) * distance,
                maxWater,
            )

            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1

        return maxWater