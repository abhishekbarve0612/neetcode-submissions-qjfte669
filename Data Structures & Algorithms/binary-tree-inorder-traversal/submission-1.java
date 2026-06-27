/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> result;
    public List<Integer> inorderTraversal(TreeNode root) {
        // result = new ArrayList<>();
        // recurse(root);
        // return result;
        return iterate(root);
    }

    public void recurse(TreeNode root) {
        if (root == null) return;
        recurse(root.left);
        result.add(root.val);
        recurse(root.right);
    }

    public List<Integer> iterate(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        Deque<TreeNode> stk = new ArrayDeque<>();

        TreeNode curr = root;
        while (curr != null || !stk.isEmpty()) {
            while (curr != null) {
                stk.add(curr);
                curr = curr.left;
            }
            curr = stk.pollLast();
            result.add(curr.val);
            curr = curr.right;
        }

        return result;
    }
}