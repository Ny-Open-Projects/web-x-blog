// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130836270
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc111_solution_6_3_____3____ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public int minDepth(TreeNode root) { // 定义函数/方法 minDepth
    if (root == null) return 0; // 若 根节点 等于 null，直接返回 0
    Deque<TreeNode> queue =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> queue
    queue.add(root); // 队列 追加 根节点);
    int depth = 0; // 把 0 存入 深度
    while (!queue.isEmpty()) { // 循环，直到不满足「取反 队列.isEmpty(」
      int size = queue.size(); // 把 队列.大小() 存入 大小
      depth += 1; // 深度累加 1
      for (int t = 0; t < size; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 大小 就继续
        TreeNode node = queue.poll(); // 把 队列.poll(); 写入 TreeNode node
        if (node.left == null && node.right == null)
          return depth; // 若 节点.左边界 等于 null 且 节点.右边界 等于 null，直接返回 深度
        if (node.left != null) queue.add(node.left); // 若 节点.左边界 不等于 null) 队列 追加 节点.左边界);
        if (node.right != null) queue.add(node.right); // 若 节点.右边界 不等于 null) 队列 追加 节点.右边界);
      }
    }
    return depth; // 返回 深度
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
    lc111_solution_6_3_____3____ s = new lc111_solution_6_3_____3____();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, 0},
      {new Integer[] {3, 9, 20, null, null, 15, 7}, 2},
      {new Integer[] {2, null, 3, null, 4, null, 5, null, 6}, 5},
      {new Integer[] {1}, 1},
      {new Integer[] {1, 2, 3, 4, 5}, 2},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      int got = s.minDepth(root); // 把 字符串.minDepth(根节点) 存入 got
      if (got != (Integer) c[1]) { // 若 got 不等于 (Integer) 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL minDepth("
                + Arrays.toString((Integer[]) c[0])
                + ")="
                + got
                + " want "
                + c[1]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
