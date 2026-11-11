// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130742026
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc144S1 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val;
    TreeNode left;
    TreeNode right; // int 值; TreeNode 左边界; TreeNode 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v){ val

    TreeNode(int v, TreeNode l, TreeNode r) {
      val = v;
      left = l;
      right = r;
    }
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals.length == 0) return null; // 若 vals.长度 等于 0，直接返回 null
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    Queue<TreeNode> q = new LinkedList<>(); // 把 new LinkedList 小于 超过 (); 写入 Queue<TreeNode> q
    q.offer(root); // 节点.offer(根节点);
    int i = 1; // 把 1 存入 下标 i
    while (i < vals.length) { // 循环，直到不满足「下标 i 小于 vals.长度」
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

  static List<Integer> preorder(TreeNode root) { // 定义函数/方法 preorder
    return null; // 返回 null
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc144S1 s = new Lc144S1(); // 把 new Lc144S1(); 写入 Lc144S1 s
    List<Integer> g1 = s.preorder(null); // 把 字符串.preorder(null); 写入 List<Integer> g1
    List<Integer> g2 = s.preorder(buildTree(new Integer[] {1, 2, 3}));
    boolean ok = true; // 把 true; 写入 boolean ok
    if (g1 != null || g2 != null) {
      ok = false;
      System.out.println("FAIL degenerate got " + g1 + " " + g2);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
