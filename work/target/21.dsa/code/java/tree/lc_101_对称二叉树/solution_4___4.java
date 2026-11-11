// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134623793
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class TreeNode { // 定义类型
  int val; // int 值;
  TreeNode left, right; // TreeNode 左边界, 右边界;

  TreeNode(int v) {
    val = v;
  } // 把 值;} 写入 TreeNode(int v){val
}

class Main { // 定义类型
  static TreeNode build(Integer[] vals) { // 定义函数/方法 build
    if (vals == null || vals.length == 0 || vals[0] == null)
      return null; // 若 vals 等于 null 或 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    java.util.LinkedList<TreeNode> q = new java.util.LinkedList<>();
    q.add(root); // 节点 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!q.isEmpty() && i < vals.length) { // 循环，直到不满足「取反 节点.isEmpty() 且 下标 i 小于 vals.长度」
      TreeNode n = q.poll(); // 把 节点.poll(); 写入 TreeNode n
      if (i < vals.length && vals[i] != null) {
        n.left = new TreeNode(vals[i]);
        q.add(n.left);
      }
      i++; // 下标 i 加一
      if (i < vals.length && vals[i] != null) {
        n.right = new TreeNode(vals[i]);
        q.add(n.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  static boolean isSymmetric(TreeNode root) { // 定义判定函数 isSymmetric
    if (root == null || (root.left == null && root.right == null)) return true;
    java.util.LinkedList<TreeNode> queue = new java.util.LinkedList<>();
    queue.add(root.left); // 队列 追加 根节点.左边界);
    queue.add(root.right); // 队列 追加 根节点.右边界);
    while (!queue.isEmpty()) { // 循环，直到不满足「取反 队列.isEmpty(」
      TreeNode left = queue.poll(); // 把 队列.poll(); 写入 TreeNode left
      TreeNode right = queue.poll(); // 把 队列.poll(); 写入 TreeNode right
      if (left == null && right == null) continue; // 若 左边界 等于 null 且 右边界 等于 null) continue;
      if (left == null || right == null) return false; // 若 左边界 等于 null 或 右边界 等于 null，直接返回 false
      if (left.val != right.val) return false; // 若 左边界.值 不等于 右边界.值，直接返回 false
      queue.add(left.left); // 队列 追加 左边界.左边界);
      queue.add(right.right); // 队列 追加 右边界.右边界);
      queue.add(left.right); // 队列 追加 左边界.右边界);
      queue.add(right.left); // 队列 追加 右边界.左边界);
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Integer[][] cases = { // 把 { 写入 Integer[][] cases
      {1, 2, 2, 3, 4, 4, 3},
      {1, 2, 3},
      {},
      {1},
    };
    boolean[] wants = {true, false, true, true}; // 把 {true, false, true, true}; 写入 boolean[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      boolean got =
          isSymmetric(build(cases[ci])); // 把 isSymmetric(build(cases[ci])); 写入 boolean got
      if (got != wants[ci]) { // 若 got 不等于 wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL case " + ci + " got " + got + " want " + wants[ci]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
