class Solution {
    public boolean isStrobogrammatic(String num) {
        Map<Character, Character> hash = new HashMap<>();

        hash.put('0', '0');
        hash.put('8', '8');
        hash.put('1', '1');
        hash.put('6', '9');
        hash.put('9', '6');

        int first = 0, last = num.length() - 1;

        while (first <= last) {
            if (num.charAt(first) != hash.getOrDefault(num.charAt(last), 'Z')) return false;
            first++;
            last--;
        }

        return true;
    }
}
