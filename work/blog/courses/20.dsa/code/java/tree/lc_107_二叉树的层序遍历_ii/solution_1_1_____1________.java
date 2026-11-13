// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144992608
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class TreeNode107 { // 定义类型
  int val; // int 值;
  TreeNode107 left, right; // TreeNode107 左边界, 右边界;

  TreeNode107(int v) {
    val = v;
  } // 把 值; } 写入 TreeNode107(int v) { val

  TreeNode107(int v, TreeNode107 l, TreeNode107 r) {
    val = v;
    left = l;
    right = r;
  }
}

class Main { // 定义类型
  List<List<Integer>> levelOrderBottom(TreeNode107 root) { // 定义函数/方法 levelOrderBottom
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    if (root == null) return res; // 若 根节点 等于 null，直接返回 结果
    Deque<TreeNode107> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode107> q
    q.add(root); // 节点 追加 根节点);
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      int sz = q.size(); // 把 节点.大小() 存入 sz
      List<Integer> level = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> level
      for (int i = 0; i < sz; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 sz 就继续
        TreeNode107 node = q.poll(); // 把 节点.poll(); 写入 TreeNode107 node
        level.add(node.val); // level 追加 节点.值);
        if (node.left != null) q.add(node.left); // 若 节点.左边界 不等于 null) 节点 追加 节点.左边界);
        if (node.right != null) q.add(node.right); // 若 节点.右边界 不等于 null) 节点 追加 节点.右边界);
      }
      res.add(0, level); // 结果 追加 0, level);
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!s.levelOrderBottom(null).isEmpty()) {
      ok = false;
      System.out.println("FAIL null");
    }
    TreeNode107 root =
        new TreeNode107(
            3, new TreeNode107(9), new TreeNode107(20, new TreeNode107(15), new TreeNode107(7)));
    List<List<Integer>> got =
        s.levelOrderBottom(root); // 把 字符串.levelOrderBottom(根节点); 写入 List<List<Integer>> got
    List<List<Integer>> want =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> want
    want.add(Arrays.asList(15, 7)); // want 追加 Arrays.asList(15, 7));
    want.add(Arrays.asList(9, 20)); // want 追加 Arrays.asList(9, 20));
    want.add(Arrays.asList(3)); // want 追加 Arrays.asList(3));
    if (!got.equals(want)) {
      ok = false;
      System.out.println("FAIL demo got=" + got);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
