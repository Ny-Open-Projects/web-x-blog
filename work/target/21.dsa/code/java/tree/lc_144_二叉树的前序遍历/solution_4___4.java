// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130742026
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc144S4 { // 定义类型
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
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    if (root == null) return res; // 若 根节点 等于 null，直接返回 结果
    res.add(root.val); // 结果 追加 根节点.值);
    res.addAll(preorder(root.left)); // 结果.addAll(preorder(根节点.左边界));
    res.addAll(preorder(root.right)); // 结果.addAll(preorder(根节点.右边界));
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc144S4 s = new Lc144S4(); // 把 new Lc144S4(); 写入 Lc144S4 s
    TreeNode t1 = buildTree(new Integer[] {1, null, 2, null, 3});
    TreeNode t2 =
        buildTree(new Integer[] {1, 2, 3}); // 把 buildTree(new Integer[]{1, 2, 3}); 写入 TreeNode t2
    TreeNode t3 = buildTree(new Integer[] {}); // 把 buildTree(new Integer[]{}); 写入 TreeNode t3
    List<Integer>[] wants =
        new List[] {Arrays.asList(1, 2, 3), Arrays.asList(1, 2, 3), Arrays.asList()};
    TreeNode[] ins = {t1, t2, t3}; // 把 {t1, t2, t3}; 写入 TreeNode[] ins
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < 3; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
      List<Integer> got = s.preorder(ins[i]); // 把 字符串.preorder(ins[下标 i]); 写入 List<Integer> got
      if (!wants[i].equals(got)) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
