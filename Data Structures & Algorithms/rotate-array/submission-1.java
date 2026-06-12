class Solution {
    public void rotate(int[] nums, int k) {
        int l = nums.length;

        int temp = -1;
        int current = temp;

        int old;
        int count = 0;
        while (count < l - 1) {
            temp++;
            current = temp;
            old = nums[current];
            do {
                int next = (current + k) % l;
                int temp1 = nums[next];
                nums[next] = old;
                old = temp1;
                count++;
                current = next;
            } while (current != temp);
        }
    }
}