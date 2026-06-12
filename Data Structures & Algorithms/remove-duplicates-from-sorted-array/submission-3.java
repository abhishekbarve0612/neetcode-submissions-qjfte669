class Solution {
    public int removeDuplicates(int[] nums) {
        int len = nums.length;

        int first = 0;
        int second = first + 1;

        while (second < len) {
            // find first not matching val
            while (second < len && nums[second] == nums[first]) second++;

            if (second < len) {
                first++;
                nums[first] = nums[second];
                second++;
            }
        }

        return first + 1;
        
    }
}