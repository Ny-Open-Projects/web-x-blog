// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130877211
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

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

  static List<List<Integer>> levelOrder(TreeNode root) { // 定义函数/方法 levelOrder
    List<List<Integer>> res = new ArrayList<>();
    if (root == null) return res;
    LinkedList<TreeNode> q = new LinkedList<>();
    q.add(root);
    while (!q.isEmpty()) {
      int n = q.size();
      List<Integer> lvl = new ArrayList<>();
      for (int k = 0; k < n; k++) {
        TreeNode x = q.poll();
        lvl.add(x.val);
        if (x.left != null) q.add(x.left);
        if (x.right != null) q.add(x.right);
      }
      res.add(lvl);
    }
    return res;
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Integer[] a = {3, 9, 20, null, 15, 7};
    Integer[] b = {};
    Integer[] c = {1};
    List<List<Integer>> got1 =
        levelOrder(buildTree(a)); // 把 levelOrder(buildTree(数组)); 写入 List<List<Integer>> got1
    if (!(got1.equals(
        Arrays.asList(Arrays.asList(3), Arrays.asList(9, 20), Arrays.asList(15, 7))))) {
      System.out.println("FAIL " + got1);
      throw new RuntimeException("FAILED");
    }
    if (!levelOrder(buildTree(b)).isEmpty()) {
      System.out.println("FAIL empty");
      throw new RuntimeException("FAILED");
    }
    if (!levelOrder(buildTree(c)).equals(Arrays.asList(Arrays.asList(1)))) {
      System.out.println("FAIL single");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
