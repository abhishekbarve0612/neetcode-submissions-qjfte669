class Solution {
    public int lengthOfLongestSubstring(String s) {
        int slow_pointer = 0;
        int max_count = 0;

        Set<Character> set = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            while (set.contains(c)) {
                set.remove(s.charAt(slow_pointer));
                slow_pointer++;
            }

            set.add(c);
            max_count = Math.max(max_count, i - slow_pointer + 1);
        }

        return max_count;
    }
}