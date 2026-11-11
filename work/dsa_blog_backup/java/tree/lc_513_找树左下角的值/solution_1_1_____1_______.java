// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145368911
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int v) {
      val = v;
    }

    TreeNode(int v, TreeNode l, TreeNode r) {
      val = v;
      left = l;
      right = r;
    }
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals.length == 0 || vals[0] == null)
      return null; // 若 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(vals[0]);
    java.util.LinkedList<TreeNode> q = new java.util.LinkedList<>();
    q.add(root);
    int i = 1;
    while (!q.isEmpty() && i < vals.length) {
      TreeNode node = q.poll();
      if (i < vals.length && vals[i] != null) {
        node.left = new TreeNode(vals[i]);
        q.add(node.left);
      }
      i++;
      if (i < vals.length && vals[i] != null) {
        node.right = new TreeNode(vals[i]);
        q.add(node.right);
      }
      i++;
    }
    return root; // 返回 根节点
  }

  static boolean sameTree(TreeNode a, TreeNode b) {
    if (a == null && b == null) return true;
    if (a == null || b == null) return false;
    if (a.val != b.val) return false;
    return sameTree(a.left, b.left) && sameTree(a.right, b.right);
  }

  static java.util.List<Integer> inorderT(TreeNode r) {
    java.util.List<Integer> l = new java.util.ArrayList<>();
    if (r != null) {
      l.addAll(inorderT(r.left));
      l.add(r.val);
      l.addAll(inorderT(r.right));
    }
    return l;
  }

  static int findBottomLeftValue(TreeNode root) {
    java.util.LinkedList<TreeNode> q = new java.util.LinkedList<>();
    q.add(root);
    int leftmost = root.val;
    while (!q.isEmpty()) {
      int n = q.size();
      leftmost = q.peek().val;
      for (int k = 0; k < n; k++) {
        TreeNode x = q.poll();
        if (x.left != null) q.add(x.left);
        if (x.right != null) q.add(x.right);
      }
    }
    return leftmost;
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (findBottomLeftValue(buildTree(new Integer[] {1, 2, 3, 4, 5, 6, 7})) != 4) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    if (findBottomLeftValue(buildTree(new Integer[] {2, 1, 3})) != 1) {
      System.out.println("FAIL2");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
