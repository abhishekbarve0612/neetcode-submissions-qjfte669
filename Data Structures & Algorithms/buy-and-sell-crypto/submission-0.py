class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minTillNow = 2 ** 32 - 1
        maxProfitTillNow = 0

        for price in prices:
            minTillNow = min(minTillNow, price)

            maxProfitTillNow = max(
                maxProfitTillNow,
                price - minTillNow,
            )

        return maxProfitTillNow