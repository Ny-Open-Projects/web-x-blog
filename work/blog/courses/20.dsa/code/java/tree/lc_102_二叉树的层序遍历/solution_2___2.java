// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130877211
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int v) {
      val = v;
    }

    TreeNode(int v, TreeNode l, TreeNode r) {
      val = v;
      left = l;
      right = r;
    }
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals.length == 0 || vals[0] == null)
      return null; // 若 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(vals[0]);
    LinkedList<TreeNode> q = new LinkedList<>();
    q.add(root);
    int i = 1;
    while (!q.isEmpty() && i < vals.length) {
      TreeNode node = q.poll();
      if (i < vals.length && vals[i] != null) {
        node.left = new TreeNode(vals[i]);
        q.add(node.left);
      }
      i++;
      if (i < vals.length && vals[i] != null) {
        node.right = new TreeNode(vals[i]);
        q.add(node.right);
      }
      i++;
    }
    return root; // 返回 根节点
  }

  // faithful translation of python solution_2___2.py (BFS by level)
  static List<List<Integer>> levelOrder(TreeNode root) { // 定义函数/方法 levelOrder
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    if (root == null) return res; // 若 根节点 等于 null，直接返回 结果
    LinkedList<TreeNode> q =
        new LinkedList<>(); // 把 new LinkedList 小于 超过 (); 写入 LinkedList<TreeNode> q
    q.add(root); // 节点 追加 根节点);
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      int len = q.size(); // 把 节点.大小() 存入 长度
      res.add(new ArrayList<Integer>()); // 结果 追加 new ArrayList 小于 Integer 超过 ());
      while (len > 0) { // 循环，直到不满足「长度 超过 0」
        TreeNode n = q.poll(); // 把 节点.poll(); 写入 TreeNode n
        res.get(res.size() - 1).add(n.val); // 结果 查找 结果.大小() 减 1) 追加 元素个数.值);
        if (n.left != null) q.add(n.left); // 若 元素个数.左边界 不等于 null) 节点 追加 元素个数.左边界);
        if (n.right != null) q.add(n.right); // 若 元素个数.右边界 不等于 null) 节点 追加 元素个数.右边界);
        len--; // 长度 减一
      }
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Integer[][] trees = { // 把 { 写入 Integer[][] trees
      {3, 9, 20, null, null, 15, 7},
      {1, 2, 3, 4, 5},
      {1},
      {},
    };
    String[] wants = { // 把 { 写入 String[] wants
      "[[3], [9, 20], [15, 7]]", "[[1], [2, 3], [4, 5]]", "[[1]]", "[]",
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < trees.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 trees.长度 就继续
      List<List<Integer>> got = levelOrder(buildTree(trees[ci]));
      if (!got.toString().equals(wants[ci])) { // 若 取反 got.toString().equals(wants[ci]
        ok = false;
        System.out.println(
            "FAIL levelOrder case " + ci + " got=" + got + " want=" + wants[ci]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
