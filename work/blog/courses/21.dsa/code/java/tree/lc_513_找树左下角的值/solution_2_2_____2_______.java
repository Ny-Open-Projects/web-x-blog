// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145368911
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc513_solution_2_2_____2_______ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public int findBottomLeftValue(TreeNode root) { // 定义函数/方法 findBottomLeftValue
    int ret = 0; // 把 0 存入 ret
    Deque<TreeNode> queue =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> queue
    queue.add(root); // 队列 追加 根节点);
    while (!queue.isEmpty()) { // 循环，直到不满足「取反 队列.isEmpty(」
      TreeNode p = queue.poll(); // 把 队列.poll(); 写入 TreeNode p
      if (p.right != null) queue.add(p.right); // 若 节点.右边界 不等于 null) 队列 追加 节点.右边界);
      if (p.left != null) queue.add(p.left); // 若 节点.左边界 不等于 null) 队列 追加 节点.左边界);
      ret = p.val; // 把 节点.值; 写入 ret
    }
    return ret; // 返回 ret
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
    lc513_solution_2_2_____2_______ s = new lc513_solution_2_2_____2_______();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new Integer[] {1, 2, 3, 4, 5, null, 6}, 4},
      {new Integer[] {1}, 1},
      {new Integer[] {1, 2, 3}, 2},
      {new Integer[] {2, 1, 3}, 1},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = build((Integer[]) c[0]); // 把 build((Integer[]) 字符[0]); 写入 TreeNode root
      int got = s.findBottomLeftValue(root); // 把 字符串.findBottomLeftValue(根节点) 存入 got
      if (got != (Integer) c[1]) { // 若 got 不等于 (Integer) 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL findBottomLeftValue("
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
