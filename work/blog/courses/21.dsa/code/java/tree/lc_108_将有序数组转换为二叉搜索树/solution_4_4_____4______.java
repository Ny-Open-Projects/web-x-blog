// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993168
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc108_solution_4_4_____4______ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public TreeNode sortedArrayToBST(int[] nums) { // 定义函数/方法 sortedArrayToBST
    if (nums.length == 0) return null; // 若 数组.长度 等于 0，直接返回 null
    int mid = nums.length / 2; // 把 数组.长度 除以 2 存入 中点
    TreeNode root = new TreeNode(nums[mid]); // 把 new TreeNode(数组[中点]); 写入 TreeNode root
    root.left =
        sortedArrayToBST(
            Arrays.copyOfRange(
                nums, 0, mid)); // 把 sortedArrayToBST(Arrays.copyOfRange(数组, 0, 中点)); 写入 左边界
    root.right = sortedArrayToBST(Arrays.copyOfRange(nums, mid + 1, nums.length));
    return root; // 返回 根节点
  }

  static List<Integer> inorder(TreeNode root) { // 定义函数/方法 inorder
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    if (root == null) return res; // 若 根节点 等于 null，直接返回 结果
    res.addAll(inorder(root.left)); // 结果.addAll(inorder(根节点.左边界));
    res.add(root.val); // 结果 追加 根节点.值);
    res.addAll(inorder(root.right)); // 结果.addAll(inorder(根节点.右边界));
    return res; // 返回 结果
  }

  static int height(TreeNode n) { // 定义函数/方法 height
    if (n == null) return 0; // 若 元素个数 等于 null，直接返回 0
    return Math.max(height(n.left), height(n.right))
        + 1; // 返回 Math.取较大值 height(元素个数.左边界), height(元素个数.右边界)) 加 1
  }

  static boolean isBalanced(TreeNode n) { // 定义判定函数 isBalanced
    if (n == null) return true; // 若 元素个数 等于 null，直接返回 true
    return Math.abs(height(n.left) - height(n.right))
            <= 1 // 返回 Math.取绝对值 height(元素个数.左边界) 减 height(元素个数.右边界)) 不超过 1
        && isBalanced(n.left)
        && isBalanced(n.right); // 且 isBalanced(元素个数.左边界) 且 isBalanced(元素个数.右边界);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc108_solution_4_4_____4______ s = new lc108_solution_4_4_____4______();
    int[][] ins = {
      {1, 2, 3}, {}, {1}, {-10, -3, 0, 5, 9}
    }; // 把 {{1,2,3}, {}, {1}, { 减 10, 减 3,0,5,9}}; 写入 int[][] ins
    int[][] wants = {
      {1, 2, 3}, {}, {1}, {-10, -3, 0, 5, 9}
    }; // 把 {{1,2,3}, {}, {1}, { 减 10, 减 3,0,5,9}}; 写入 int[][] wants
    int[] rootWants = {2, 0, 1, 0}; // 把 {2, 0, 1, 0}; 写入 int[] rootWants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      TreeNode root =
          s.sortedArrayToBST(ins[i]); // 把 字符串.sortedArrayToBST(ins[下标 i]); 写入 TreeNode root
      List<Integer> got = inorder(root); // 把 inorder(根节点); 写入 List<Integer> got
      List<Integer> want = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> want
      for (int v : wants[i]) want.add(v); // for (int 值 : wants[下标 i]) want 追加 值);
      if (!got.equals(want)) {
        ok = false;
        System.out.println("FAIL inorder " + Arrays.toString(ins[i]) + "=" + got + " want " + want);
      }
      if (!isBalanced(root)) {
        ok = false;
        System.out.println("FAIL not balanced " + Arrays.toString(ins[i]));
      }
      if (ins[i].length > 0 && root.val != rootWants[i]) {
        ok = false;
        System.out.println("FAIL root " + root.val + " want " + rootWants[i]);
      }
      if (ins[i].length == 0 && root != null) {
        ok = false;
        System.out.println("FAIL empty should be null");
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
