class Solution {
    public int subarraySum(int[] nums, int k) {
                Map<Integer, Integer> map = new HashMap<>();
        int result = 0;
        int currentSum = 0;
        map.put(0, 1);

        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            if (map.containsKey(currentSum - k)) {
                result += map.get(currentSum - k);
            }
            map.put(currentSum, map.getOrDefault(currentSum, 0) + 1);
        }

        return result;
    }
}