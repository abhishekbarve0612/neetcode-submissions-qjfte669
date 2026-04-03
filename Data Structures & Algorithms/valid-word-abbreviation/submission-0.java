class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int first = 0, second = 0;
        while (second < abbr.length()) {
            int temp = second;
            while (temp < abbr.length() && Character.isDigit(abbr.charAt(temp))) temp++;
            if (temp > second) {
                if (abbr.charAt(second) == '0') return false;
                String digit = abbr.substring(second, temp);
                int num = Integer.parseInt(digit);
                first += num;
                second = temp;
                if (first > word.length()) return false;
            if (second < abbr.length() && first < word.length() && word.charAt(first) != abbr.charAt(second)) return false;
            } else {
            if (second < abbr.length() && first < word.length() && word.charAt(first) != abbr.charAt(second)) return false;
                first++;
                second++;
                
            }
            
            
        }
      return first == word.length();
    }
}