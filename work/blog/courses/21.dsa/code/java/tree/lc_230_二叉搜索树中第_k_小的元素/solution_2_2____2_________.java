// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145053587
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc230S2 { // 定义类型
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

  static int count(TreeNode node) { // 定义函数/方法 count
    if (node == null) return 0; // 若 节点 等于 null，直接返回 0
    return 1 + count(node.left) + count(node.right); // 返回 1 加 计数(节点.左边界) 加 计数(节点.右边界)
  }

  static int kthSmallest(TreeNode root, int k) { // 定义函数/方法 kthSmallest
    while (root != null) { // 循环，直到不满足「根节点 不等于 null」
      int leftCount = count(root.left); // 把 计数(根节点.左边界) 存入 leftCount
      if (leftCount == k - 1) return root.val; // 若 leftCount 等于 下标 k 减 1，直接返回 根节点.值
      else if (leftCount < k - 1) {
        k -= leftCount + 1;
        root = root.right;
      } else {
        root = root.left;
      } // 否则
    }
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc230S2 s = new Lc230S2(); // 把 new Lc230S2(); 写入 Lc230S2 s
    TreeNode root = buildTree(new Integer[] {3, 1, 4, null, 2});
    int[] ks = {1, 2, 3, 4}; // 把 {1, 2, 3, 4}; 写入 int[] ks
    int[] wants = {1, 2, 3, 4}; // 把 {1, 2, 3, 4}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ks.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ks.长度 就继续
      int got = s.kthSmallest(root, ks[i]); // 把 字符串.kthSmallest(根节点, ks[下标 i]) 存入 got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL k=" + ks[i] + " got " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
