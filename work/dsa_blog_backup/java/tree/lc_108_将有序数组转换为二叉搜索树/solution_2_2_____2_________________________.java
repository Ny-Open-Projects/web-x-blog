// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993168
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

  static int[] numsArr; // static int[] numsArr;

  static TreeNode build(int l, int r) {
    if (l > r) return null;
    int m = l + (r - l) / 2;
    return new TreeNode(numsArr[m], build(l, m - 1), build(m + 1, r));
  }

  static TreeNode sortedArrayToBST(int[] nums) {
    numsArr = nums;
    return build(0, nums.length - 1);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (!inorderT(sortedArrayToBST(new int[] {1, 2, 3})).equals(Arrays.asList(1, 2, 3))) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    if (!inorderT(sortedArrayToBST(new int[] {-10, -3, 0, 5, 9}))
        .equals(Arrays.asList(-10, -3, 0, 5, 9))) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
