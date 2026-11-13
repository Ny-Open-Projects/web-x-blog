// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091703
package com.webfault.dsa; // 引入依赖

class lc700_search { // 定义类型
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

  TreeNode searchBST(TreeNode root, int val) { // 定义函数/方法 searchBST
    while (root != null) { // 循环，直到不满足「根节点 不等于 null」
      if (root.val == val) return root; // 若 根节点.值 等于 值，直接返回 根节点
      root = val < root.val ? root.left : root.right; // 把 值 小于 根节点.值 ? 根节点.左边界 : 根节点.右边界; 写入 根节点
    }
    return null; // 返回 null
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc700_search s = new lc700_search(); // 把 new lc700_search(); 写入 lc700_search s
    TreeNode root =
        new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7));
    boolean ok = true; // 把 true; 写入 boolean ok
    TreeNode r1 = s.searchBST(root, 2); // 把 字符串.searchBST(根节点, 2); 写入 TreeNode r1
    if (!(r1 != null && r1.val == 2)) {
      ok = false;
      System.out.println("FAIL case1");
    }
    TreeNode r2 = s.searchBST(root, 5); // 把 字符串.searchBST(根节点, 5); 写入 TreeNode r2
    if (r2 != null) {
      ok = false;
      System.out.println("FAIL case2");
    }
    TreeNode r3 = s.searchBST(root, 4); // 把 字符串.searchBST(根节点, 4); 写入 TreeNode r3
    if (!(r3 != null && r3.val == 4)) {
      ok = false;
      System.out.println("FAIL case3");
    }
    TreeNode r4 = s.searchBST(null, 1); // 把 字符串.searchBST(null, 1); 写入 TreeNode r4
    if (r4 != null) {
      ok = false;
      System.out.println("FAIL case4");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
