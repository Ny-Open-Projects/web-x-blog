// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130836270
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc111_solution_1___1 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public int minDepth(TreeNode root) { // 定义函数/方法 minDepth
    if (root == null) return 0; // 若 根节点 等于 null，直接返回 0
    Deque<TreeNode> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> q
    Deque<Integer> lv = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> lv
    q.add(root); // 节点 追加 根节点);
    lv.add(1); // lv 追加 1);
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      TreeNode n = q.poll(); // 把 节点.poll(); 写入 TreeNode n
      int l = lv.poll(); // 把 lv.poll() 存入 左指针
      if (n.left == null && n.right == null)
        return l; // 若 元素个数.左边界 等于 null 且 元素个数.右边界 等于 null，直接返回 左指针
      if (n.left != null) {
        q.add(n.left);
        lv.add(l + 1);
      } // 若 元素个数.左边界 不等于 null) { 节点 追加 元素个数.左边界); lv 追加 左指针 加 1); }
      if (n.right != null) {
        q.add(n.right);
        lv.add(l + 1);
      } // 若 元素个数.右边界 不等于 null) { 节点 追加 元素个数.右边界); lv 追加 左指针 加 1); }
    }
    return 0; // 返回 0
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
    lc111_solution_1___1 s =
        new lc111_solution_1___1(); // 把 new lc111_solution_1___1(); 写入 lc111_solution_1___1 s
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
