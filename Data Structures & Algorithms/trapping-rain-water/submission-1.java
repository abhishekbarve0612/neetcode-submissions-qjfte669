class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int maxFromLeft = height[left], maxFromRight = height[right];
        int total = 0;

        while (left < right) {
            if (maxFromLeft < maxFromRight) {
                left++;
                maxFromLeft = Math.max(maxFromLeft, height[left]);
                total += Math.max(
                    0,
                    maxFromLeft - height[left]
                );
            } else {
                right--;
                maxFromRight = Math.max(maxFromRight, height[right]);
                total += Math.max(
                    0,
                    maxFromRight - height[right]
                );
            }
        }

        return total;
    }
}
