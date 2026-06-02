class Solution {
    public int maxArea(int[] height) {
        int maxCapacity = 0;

        int first = 0, last = height.length - 1;

        while (first < last) {
            int currentCapacity = Math.min(height[first], height[last]) * (last - first);
            maxCapacity = Math.max(maxCapacity, currentCapacity);
            if (height[first] < height[last]) {
                first++;
            } else {
                last--;
            }
        }

        return maxCapacity;
    }
}