// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134622591
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc100_solution_3___3 { // 定义类型
  static class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int v) {
      val = v;
    }
  }

  public static boolean isSameTree(
      TreeNode p, TreeNode q) { // public static boolean isSameTree(TreeNode 节点, TreeNode 节点) {
    if (p == null && q == null) return true; // 若 节点 等于 null 且 节点 等于 null，直接返回 true
    if (p == null || q == null) return false; // 若 节点 等于 null 或 节点 等于 null，直接返回 false
    if (p.val != q.val) return false; // 若 节点.值 不等于 节点.值，直接返回 false
    return isSameTree(p.left, q.left)
        && isSameTree(
            p.right, q.right); // 返回 isSameTree(节点.左边界, 节点.左边界) 且 isSameTree(节点.右边界, 节点.右边界)
  }

  static TreeNode build(Integer[] a) { // 定义函数/方法 build
    if (a.length == 0 || a[0] == null) return null; // 若 数组.长度 等于 0 或 数组[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(a[0]); // 把 new TreeNode(数组[0]); 写入 TreeNode root
    Deque<TreeNode> queue =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> queue
    queue.add(root); // 队列 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!queue.isEmpty() && i < a.length) { // 循环，直到不满足「取反 队列.isEmpty() 且 下标 i 小于 数组.长度」
      TreeNode node = queue.poll(); // 把 队列.poll(); 写入 TreeNode node
      if (i < a.length && a[i] != null) {
        node.left = new TreeNode(a[i]);
        queue.add(node.left);
      }
      i++; // 下标 i 加一
      if (i < a.length && a[i] != null) {
        node.right = new TreeNode(a[i]);
        queue.add(node.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, null, true},
      {new Integer[] {1, 2, 3}, new Integer[] {1, 2, 3}, true},
      {new Integer[] {1, 2}, new Integer[] {1, null, 2}, false},
      {new Integer[] {1, 2, 1}, new Integer[] {1, 1, 2}, false},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode p = c[0] == null ? null : build((Integer[]) c[0]);
      TreeNode q = c[1] == null ? null : build((Integer[]) c[1]);
      boolean got = isSameTree(p, q); // 把 isSameTree(节点, 节点); 写入 boolean got
      if (got != (Boolean) c[2]) { // 若 got 不等于 (Boolean) 字符[2]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL isSameTree("
                + Arrays.toString((Integer[]) c[0])
                + ","
                + Arrays.toString((Integer[]) c[1])
                + ")="
                + got
                + " want "
                + c[2]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
