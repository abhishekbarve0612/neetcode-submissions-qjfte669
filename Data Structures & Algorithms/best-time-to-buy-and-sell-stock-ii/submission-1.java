class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int currentProfit = 0;

        int boughtAt = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                currentProfit = Math.max(
                    prices[i] - prices[boughtAt], currentProfit);
            } else {
                // book the profit
                maxProfit += currentProfit;
                currentProfit = 0;
                boughtAt = i;
            }
        }
        if (currentProfit != 0) maxProfit += currentProfit;

        return maxProfit;
    }
}