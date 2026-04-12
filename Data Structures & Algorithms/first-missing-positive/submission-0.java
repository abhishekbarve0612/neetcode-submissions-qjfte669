class Solution {
    public int firstMissingPositive(int[] nums) {
        boolean[] seen = new boolean[nums.length + 1];

        for (int num: nums) {
            if (num > 0 && num <= nums.length) {
                seen[num] = true;
            }
        }

        for (int i = 1; i < seen.length; i++) {
            if (seen[i] == false) return i;
        }

        return nums.length + 1;
    }
}