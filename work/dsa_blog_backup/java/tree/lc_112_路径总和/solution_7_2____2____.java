// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
package com.webfault.dsa; // 引入依赖

class lc112 { // 定义类型
  static class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int v) {
      val = v;
    }
  }

  boolean hasPathSum(TreeNode root, int targetSum) { // 定义函数/方法 hasPathSum
    if (root == null) return false; // 若 根节点 等于 null，直接返回 false
    if (root.left == null && root.right == null)
      return root.val == targetSum; // 若 根节点.左边界 等于 null 且 根节点.右边界 等于 null，直接返回 根节点.值 等于 targetSum
    return hasPathSum(root.left, targetSum - root.val)
        || hasPathSum(root.right, targetSum - root.val);
  }

  static TreeNode buildTree() { // 定义函数/方法 buildTree
    TreeNode root = new TreeNode(5); // 把 new TreeNode(5); 写入 TreeNode root
    root.left = new TreeNode(4); // 把 new TreeNode(4); 写入 左边界
    root.right = new TreeNode(8); // 把 new TreeNode(8); 写入 右边界
    root.left.left = new TreeNode(11); // 把 new TreeNode(11); 写入 左边界
    root.left.left.left = new TreeNode(7); // 把 new TreeNode(7); 写入 左边界
    root.left.left.right = new TreeNode(2); // 把 new TreeNode(2); 写入 右边界
    root.right.left = new TreeNode(13); // 把 new TreeNode(13); 写入 左边界
    root.right.right = new TreeNode(4); // 把 new TreeNode(4); 写入 右边界
    root.right.right.right = new TreeNode(1); // 把 new TreeNode(1); 写入 右边界
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc112 s = new lc112(); // 把 new lc112(); 写入 lc112 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.hasPathSum(null, 0) != false) {
      ok = false;
      System.out.println("FAIL null");
    }
    if (s.hasPathSum(buildTree(), 22) != true) {
      ok = false;
      System.out.println("FAIL 22");
    }
    if (s.hasPathSum(buildTree(), 100) != false) {
      ok = false;
      System.out.println("FAIL 100");
    }
    if (s.hasPathSum(new TreeNode(5), 5) != true) {
      ok = false;
      System.out.println("FAIL single 5");
    }
    if (s.hasPathSum(buildTree(), 27) != true) {
      ok = false;
      System.out.println("FAIL 27");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
