// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc104S6 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val;
    TreeNode left;
    TreeNode right; // int 值; TreeNode 左边界; TreeNode 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v){ val
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals.length == 0) return null; // 若 vals.长度 等于 0，直接返回 null
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    Queue<TreeNode> q = new LinkedList<>(); // 把 new LinkedList 小于 超过 (); 写入 Queue<TreeNode> q
    q.offer(root); // 节点.offer(根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!q.isEmpty() && i < vals.length) { // 循环，直到不满足「取反 节点.isEmpty() 且 下标 i 小于 vals.长度」
      TreeNode node = q.poll(); // 把 节点.poll(); 写入 TreeNode node
      if (i < vals.length && vals[i] != null) {
        node.left = new TreeNode(vals[i]);
        q.offer(node.left);
      }
      i++; // 下标 i 加一
      if (i < vals.length && vals[i] != null) {
        node.right = new TreeNode(vals[i]);
        q.offer(node.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  static int maxDepth(TreeNode root) { // 定义函数/方法 maxDepth
    if (root == null) return 0; // 若 根节点 等于 null，直接返回 0
    return 1
        + Math.max(
            maxDepth(root.left),
            maxDepth(root.right)); // 返回 1 加 Math.取较大值 maxDepth(根节点.左边界), maxDepth(根节点.右边界))
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc104S6 s = new Lc104S6(); // 把 new Lc104S6(); 写入 Lc104S6 s
    TreeNode t = buildTree(new Integer[] {3, 9, 20, null, null, 15, 7});
    int[] got = {
      s.maxDepth(t), s.maxDepth(null)
    }; // 把 { 字符串.maxDepth(另一字符串), 字符串.maxDepth(null) }; 写入 int[] got
    int[] want = {3, 0}; // 把 {3, 0}; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got[i] + " want " + want[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
