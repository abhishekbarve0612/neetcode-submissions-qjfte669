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
    public List<Integer> preorderTraversal(TreeNode root) {
        result = new ArrayList<>();
        recurse(root);
        return result;
    }

    public void recurse(TreeNode root) {
        if (root == null) return;
        result.add(root.val);
        recurse(root.left);
        recurse(root.right);
    }

    public List<Integer> iterate(TreeNode root) {
        Deque<TreeNode> stk = new ArrayDeque<>();

        stk.add(root);
        List<Integer> result = new ArrayList<>();

        while (!stk.isEmpty()) {
            TreeNode node = stk.pollFirst();

            result.add(node.val);
            if (node.right != null) stk.add(node.right);
            if (node.left != null) stk.add(node.left);
        }

        return result;
    }
}