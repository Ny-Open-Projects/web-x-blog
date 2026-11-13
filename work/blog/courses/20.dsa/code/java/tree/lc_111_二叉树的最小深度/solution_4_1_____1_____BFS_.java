// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130836270
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

  static int minDepth(TreeNode root) {
    if (root == null) return 0;
    if (root.left == null) return 1 + minDepth(root.right);
    if (root.right == null) return 1 + minDepth(root.left);
    return 1 + Math.min(minDepth(root.left), minDepth(root.right));
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Object[][] ins = {{3, 9, 20, null, 15, 7}, {1, 2, 3, 4, 5, null, null, null, 6}, {}};
    int[] ws = {2, 3, 0}; // 把 {2,3,0}; 写入 int[] ws
    // use Integer arrays
    Integer[][][] data = {{{3, 9, 20, null, 15, 7}}, {{1, 2, 3, 4, 5, null, null, null, 6}}, {{}}};
    boolean ok = true; // 把 true; 写入 boolean ok
    Integer[] a1 = {3, 9, 20, null, 15, 7};
    Integer[] a2 = {1, 2, 3, 4, 5, null, null, null, 6};
    Integer[] a3 = {};
    Integer[][] arr = {a1, a2, a3};
    int[] want = {3, 2, 0}; // 把 {a1,a2,a3}; int[] want 赋值为 {3,2,0}; 写入 Integer[][] arr
    for (int i = 0; i < arr.length; i++) {
      int got = minDepth(buildTree(arr[i]));
      if (got != want[i]) {
        ok = false;
        System.out.println("FAIL " + got);
      }
    } // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
