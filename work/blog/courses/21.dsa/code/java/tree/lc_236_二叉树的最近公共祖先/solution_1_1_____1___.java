// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083302
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc236_solution_1_1_____1___ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public TreeNode lowestCommonAncestor(
      TreeNode root, TreeNode p, TreeNode q) { // 定义函数/方法 lowestCommonAncestor
    if (root == null || root == p || root == q) { // 若 根节点 等于 null 或 根节点 等于 节点 或 根节点 等于 节点
      return root; // 返回 根节点
    }
    TreeNode left =
        lowestCommonAncestor(
            root.left, p, q); // 把 lowestCommonAncestor(根节点.左边界, 节点, 节点); 写入 TreeNode left
    TreeNode right =
        lowestCommonAncestor(
            root.right, p, q); // 把 lowestCommonAncestor(根节点.右边界, 节点, 节点); 写入 TreeNode right
    if (left != null && right != null) { // 若 左边界 不等于 null 且 右边界 不等于 null
      return root; // 返回 根节点
    }
    return left != null ? left : right; // 返回 左边界 不等于 null ? 左边界 : 右边界
  }

  static TreeNode find(TreeNode root, int val) { // 定义函数/方法 find
    if (root == null) return null; // 若 根节点 等于 null，直接返回 null
    if (root.val == val) return root; // 若 根节点.值 等于 值，直接返回 根节点
    TreeNode l = find(root.left, val); // 把 find(根节点.左边界, 值); 写入 TreeNode l
    return l != null ? l : find(root.right, val); // 返回 左指针 不等于 null ? 左指针 : find(根节点.右边界, 值)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc236_solution_1_1_____1___ s = new lc236_solution_1_1_____1___();
    TreeNode root = new TreeNode(3); // 把 new TreeNode(3); 写入 TreeNode root
    root.left = new TreeNode(5); // 把 new TreeNode(5); 写入 左边界
    root.right = new TreeNode(1); // 把 new TreeNode(1); 写入 右边界
    root.left.left = new TreeNode(6); // 把 new TreeNode(6); 写入 左边界
    root.left.right = new TreeNode(2); // 把 new TreeNode(2); 写入 右边界
    root.right.left = new TreeNode(0); // 把 new TreeNode(0); 写入 左边界
    root.right.right = new TreeNode(8); // 把 new TreeNode(8); 写入 右边界
    root.left.right.left = new TreeNode(7); // 把 new TreeNode(7); 写入 左边界
    root.left.right.right = new TreeNode(4); // 把 new TreeNode(4); 写入 右边界
    int[][] cases = {{5, 1, 3}, {5, 4, 5}, {6, 8, 3}, {7, 4, 2}, {5, 5, 5}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      TreeNode p = find(root, c[0]); // 把 find(根节点, 字符[0]); 写入 TreeNode p
      TreeNode q = find(root, c[1]); // 把 find(根节点, 字符[1]); 写入 TreeNode q
      TreeNode ans =
          s.lowestCommonAncestor(
              root, p, q); // 把 字符串.lowestCommonAncestor(根节点, 节点, 节点); 写入 TreeNode ans
      int got = ans == null ? -1 : ans.val; // 把 答案 等于 null ? 减 1 : 答案.值 存入 got
      if (got != c[2]) { // 若 got 不等于 字符[2]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL LCA(" + c[0] + "," + c[1] + ")=" + got + " want " + c[2]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
