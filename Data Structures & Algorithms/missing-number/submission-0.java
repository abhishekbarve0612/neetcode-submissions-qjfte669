class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num: nums) {
            seen.add(num);
        }

        for (int i = 0; i < nums.length + 1; i++) {
            if (!seen.contains(i)) return i;
        }

        return -1;
        
    }
}
