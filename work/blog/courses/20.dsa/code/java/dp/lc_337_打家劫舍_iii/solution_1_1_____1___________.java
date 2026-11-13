// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850725
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class TreeNode337 {
  int val;
  TreeNode337 left, right;

  TreeNode337(int v) {
    val = v;
  }

  TreeNode337(int v, TreeNode337 l, TreeNode337 r) {
    val = v;
    left = l;
    right = r;
  }
} // 定义类型

class Main { // 定义类型
  int rob(TreeNode337 root) { // 定义函数/方法 rob
    int[] st = dfs(root); // 把 dfs(根节点); 写入 int[] st
    return Math.max(st[0], st[1]); // 返回 Math.取较大值 st[0], st[1])
  }

  int[] dfs(TreeNode337 node) { // 定义函数/方法 dfs
    if (node == null) return new int[] {0, 0}; // 若 节点 等于 null，直接返回 new int[]{0, 0}
    int[] l = dfs(node.left); // 把 dfs(节点.左边界); 写入 int[] l
    int[] r = dfs(node.right); // 把 dfs(节点.右边界); 写入 int[] r
    int selected = node.val + l[1] + r[1]; // 把 节点.值 加 左指针[1] 加 右指针[1] 存入 selected
    int notSelected = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);
    return new int[] {selected, notSelected}; // 返回 new int[]{selected, notSelected}
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.rob(null) != 0) {
      ok = false;
      System.out.println("FAIL null");
    }
    TreeNode337 single = new TreeNode337(5); // 把 new TreeNode337(5); 写入 TreeNode337 single
    if (s.rob(single) != 5) {
      ok = false;
      System.out.println("FAIL single");
    }
    TreeNode337 root =
        new TreeNode337(
            3,
            new TreeNode337(2, null, new TreeNode337(3)),
            new TreeNode337(
                3, null, new TreeNode337(1))); // new TreeNode337(3, null, new TreeNode337(1)));
    if (s.rob(root) != 7) {
      ok = false;
      System.out.println("FAIL demo got=" + s.rob(root));
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
