class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = height[left], rightMax = height[right];
        int total = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                left++;
                leftMax = Math.max(leftMax, height[left]);
                total += Math.max(
                    0,
                    leftMax - height[left]
                );
            } else {
                right--;
                rightMax = Math.max(rightMax, height[right]);
                total += Math.max(
                    0,
                    rightMax - height[right]
                );

            }
        }

        return total;
    }
}
