// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145084192
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc404S2 { // 定义类型
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

  static int sumOfLeftLeaves(TreeNode root) { // 定义函数/方法 sumOfLeftLeaves
    int[] leftSum = {0}; // 把 {0}; 写入 int[] leftSum
    traverse(root, leftSum); // traverse(根节点, leftSum);
    return leftSum[0]; // 返回 leftSum[0]
  }

  static void traverse(TreeNode node, int[] leftSum) { // 定义函数/方法 traverse
    if (node == null) return; // 若 节点 等于 null) return;
    TreeNode left = node.left; // 把 节点.左边界; 写入 TreeNode left
    if (left != null
        && left.left == null
        && left.right == null) { // 若 左边界 不等于 null 且 左边界.左边界 等于 null 且 左边界.右边界 等于 null
      leftSum[0] += left.val; // leftSum[0]累加 左边界.值
    }
    traverse(node.left, leftSum); // traverse(节点.左边界, leftSum);
    traverse(node.right, leftSum); // traverse(节点.右边界, leftSum);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int a = sumOfLeftLeaves(null); // 把 sumOfLeftLeaves(null) 存入 数组
    if (a != 0) throw new RuntimeException("FAILED a=" + a);
    int b =
        sumOfLeftLeaves(
            buildTree(
                new Integer[] {
                  1, null, 2
                })); // 把 sumOfLeftLeaves(buildTree(new Integer[]{1,null,2})) 存入 b
    if (b != 0)
      throw new RuntimeException(
          "FAILED b=" + b); // 若 b 不等于 0) throw new RuntimeException(「FAILED b 赋值为 」 加 b);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
