// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131631290
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

/** LeetCode 98. 验证二叉搜索树 方案5：递归上下界（lower/upper bound）——按博客算法实现， 每棵子树的所有值必须落在 (lo, hi) 开区间内。 */
class lc98_solution_5 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      this.val = v;
    } // 把 值; } 写入 值
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals == null || vals.length == 0 || vals[0] == null)
      return null; // 若 vals 等于 null 或 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    java.util.LinkedList<TreeNode> q = new java.util.LinkedList<>();
    q.add(root); // 节点 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!q.isEmpty() && i < vals.length) { // 循环，直到不满足「取反 节点.isEmpty() 且 下标 i 小于 vals.长度」
      TreeNode node = q.poll(); // 把 节点.poll(); 写入 TreeNode node
      if (i < vals.length && vals[i] != null) {
        node.left = new TreeNode(vals[i]);
        q.add(node.left);
      }
      i++; // 下标 i 加一
      if (i < vals.length && vals[i] != null) {
        node.right = new TreeNode(vals[i]);
        q.add(node.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  static boolean isValidBST(TreeNode root) { // 定义判定函数 isValidBST
    return check(
        root, Long.MIN_VALUE, Long.MAX_VALUE); // 返回 check(根节点, Long.MIN_VALUE, Long.MAX_VALUE)
  }

  private static boolean check(TreeNode n, long lo, long hi) {
    if (n == null) return true; // 若 元素个数 等于 null，直接返回 true
    if ((long) n.val <= lo || (long) n.val >= hi)
      return false; // 若 (long) 元素个数.值 不超过 左边界 或 (long) 元素个数.值 不低于 右边界，直接返回 false
    return check(n.left, lo, n.val) && check(n.right, n.val, hi);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Integer[][] ins = { // 把 { 写入 Integer[][] ins
      {},
      {1},
      {1, 1},
      {2, 1, 3},
      {5, 1, 4, null, null, 3, 6}, // 反例：4 的左子 3 < 5
      {10, 5, 15, null, null, 6, 20}, // 反例：6 < 10
      {3, 1, 5, 0, 2, 4, 6, null, null, null, 3}, // 反例：4 的左子 3 == 上界
    };
    boolean[] wants = {true, true, false, true, false, false, false};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < ins.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 ins.长度 就继续
      boolean got =
          isValidBST(buildTree(ins[k])); // 把 isValidBST(buildTree(ins[下标 k])); 写入 boolean got
      if (got != wants[k]) { // 若 got 不等于 wants[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL isValidBST("
                + Arrays.toString(ins[k])
                + ")="
                + got
                + " want "
                + wants[k]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
