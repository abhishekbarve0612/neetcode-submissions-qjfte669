class Solution {
    public void sortColors(int[] nums) {
        int start = 0, end = nums.length - 1;
        int zero = 0, two = end;
        
        while (start <= end) {
            while (start < end && nums[start] == 2) {
                int temp = nums[start];
                nums[start] = nums[two];
                nums[two] = temp;
                end--;
                two--;
            }
            if (nums[start] == 0) {
                int temp = nums[start];
                nums[start] = nums[zero];
                nums[zero] = temp;
                zero++;
            }
            
            start++;
        }
    }
}