// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089162
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc543_solution_2___2 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  private int ans; // private int 答案;

  public int diameterOfBinaryTree(TreeNode root) { // 定义函数/方法 diameterOfBinaryTree
    ans = 0; // 把 0; 写入 答案
    maxDepth(root); // maxDepth(根节点);
    return ans; // 返回 答案
  }

  private int maxDepth(TreeNode node) { // 定义函数/方法 maxDepth
    if (node == null) return 0; // 若 节点 等于 null，直接返回 0
    int left = maxDepth(node.left); // 把 maxDepth(节点.左边界) 存入 左边界
    int right = maxDepth(node.right); // 把 maxDepth(节点.右边界) 存入 右边界
    ans = Math.max(ans, left + right); // 把 Math.取较大值 答案, 左边界 加 右边界); 写入 答案
    return Math.max(left, right) + 1; // 返回 Math.取较大值 左边界, 右边界) 加 1
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
    lc543_solution_2___2 s =
        new lc543_solution_2___2(); // 把 new lc543_solution_2___2(); 写入 lc543_solution_2___2 s
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, 0},
      {new Integer[] {1, 2}, 1},
      {new Integer[] {1, 2, 3, 4, 5}, 3},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      int got = s.diameterOfBinaryTree(root); // 把 字符串.diameterOfBinaryTree(根节点) 存入 got
      if (got != (Integer) c[1]) { // 若 got 不等于 (Integer) 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL diameterOfBinaryTree("
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
