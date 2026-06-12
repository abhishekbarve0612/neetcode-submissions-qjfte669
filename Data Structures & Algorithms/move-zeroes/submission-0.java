class Solution {
    public void moveZeroes(int[] nums) {
        int len = nums.length;
        int start = 0;
        int zero = 0;

        while (start < len) {
            // find first non zero
            while (start < len && nums[start] == 0) start++;

            if (start < len) {
                nums[zero] = nums[start];
                zero++;
            }
            start++;
        }

        for (int i = zero; i < len; i++) {
            nums[i] = 0;
        }  
    }
}