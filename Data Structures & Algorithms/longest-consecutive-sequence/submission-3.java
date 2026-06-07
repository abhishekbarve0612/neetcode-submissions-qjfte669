class Solution {
    public int longestConsecutive(int[] nums) {
        
        Set<Integer> set = new HashSet<>();

        for (int num: nums) {
            set.add(num);
        }

        int maxLength = 0;

        for (int num: set) {
            if (set.contains(num - 1)) continue;
            else {
                int currLength = 1;
                int temp = num;
                while (set.contains(temp + 1)) {
                    currLength++;
                    temp++;
                }

                maxLength = Math.max(currLength, maxLength);
            }
        }

        return maxLength;
    }
}
