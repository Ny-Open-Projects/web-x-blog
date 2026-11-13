// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145052590
package com.webfault.dsa; // 引入依赖

class Lc222 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val

    TreeNode(int v, TreeNode l, TreeNode r) {
      val = v;
      left = l;
      right = r;
    }
  }

  static TreeNode buildComplete() { // 定义函数/方法 buildComplete
    TreeNode n1 = new TreeNode(1); // 把 new TreeNode(1); 写入 TreeNode n1
    TreeNode n2 = new TreeNode(2); // 把 new TreeNode(2); 写入 TreeNode n2
    TreeNode n3 = new TreeNode(3); // 把 new TreeNode(3); 写入 TreeNode n3
    TreeNode n4 = new TreeNode(4); // 把 new TreeNode(4); 写入 TreeNode n4
    TreeNode n5 = new TreeNode(5); // 把 new TreeNode(5); 写入 TreeNode n5
    TreeNode n6 = new TreeNode(6); // 把 new TreeNode(6); 写入 TreeNode n6
    n1.left = n2;
    n1.right = n3; // 把 n2; n1.右边界 赋值为 n3; 写入 左边界
    n2.left = n4;
    n2.right = n5; // 把 n4; n2.右边界 赋值为 n5; 写入 左边界
    n3.left = n6; // 把 n6; 写入 左边界
    return n1; // 返回 n1
  }

  int countNodes(TreeNode root) { // 定义函数/方法 countNodes
    if (root == null) return 0; // 若 根节点 等于 null，直接返回 0
    return countNodes(root.left)
        + countNodes(root.right)
        + 1; // 返回 countNodes(根节点.左边界) 加 countNodes(根节点.右边界) 加 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc222 s = new Lc222(); // 把 new Lc222(); 写入 Lc222 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.countNodes(null) != 0) {
      ok = false;
      System.out.println("FAIL null");
    }
    if (s.countNodes(s.buildComplete()) != 6) {
      ok = false;
      System.out.println("FAIL tree");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
