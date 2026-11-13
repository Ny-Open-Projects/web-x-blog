// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145084192
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc404S1 { // 定义类型
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
    java.util.Queue<TreeNode> q = new java.util.LinkedList<>();
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

  static boolean isLeaf(TreeNode n) {
    return n != null && n.left == null && n.right == null;
  }

  static int sumOfLeftLeaves(TreeNode root) { // 定义函数/方法 sumOfLeftLeaves
    if (root == null) return 0; // 若 根节点 等于 null，直接返回 0
    int total = 0; // 把 0 存入 总和
    Deque<TreeNode> stack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> stack
    stack.push(root); // 把 根节点 压入栈/数组尾部
    while (!stack.isEmpty()) { // 循环，直到不满足「取反 栈.isEmpty(」
      TreeNode node = stack.pop(); // 弹出栈顶元素
      if (node.left != null) { // 若 节点.左边界 不等于 null
        if (isLeaf(node.left)) total += node.left.val; // 若 isLeaf(节点.左边界)) 总和 累加 节点.左边界.值;
        else stack.push(node.left); // 否则
      }
      if (node.right != null) stack.push(node.right); // 若 节点.右边界 不等于 null) 栈 追加 节点.右边界);
    }
    return total; // 返回 总和
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int a = sumOfLeftLeaves(buildTree(new Integer[] {3, 9, 20, null, null, 15, 7}));
    if (a != 24) throw new RuntimeException("FAILED a=" + a);
    int b = sumOfLeftLeaves(null); // 把 sumOfLeftLeaves(null) 存入 b
    if (b != 0)
      throw new RuntimeException(
          "FAILED b=" + b); // 若 b 不等于 0) throw new RuntimeException(「FAILED b 赋值为 」 加 b);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
