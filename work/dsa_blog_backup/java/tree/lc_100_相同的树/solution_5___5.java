// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134622591
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

  static boolean isSameTree(TreeNode p, TreeNode q) {
    return sameTree(p, q);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Integer[] a1 = {1, 2, 3};
    Integer[] a2 = {1, 2, 3};
    Integer[] a3 = {1, 2, null};
    boolean t1 =
        isSameTree(
            buildTree(a1),
            buildTree(a2)); // 把 isSameTree(buildTree(a1),buildTree(a2)); 写入 boolean t1
    boolean t2 =
        isSameTree(
            buildTree(a1),
            buildTree(a3)); // 把 isSameTree(buildTree(a1),buildTree(a3)); 写入 boolean t2
    boolean t3 = isSameTree(null, null); // 把 isSameTree(null,null); 写入 boolean t3
    if (!(t1 && !t2 && t3)) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
