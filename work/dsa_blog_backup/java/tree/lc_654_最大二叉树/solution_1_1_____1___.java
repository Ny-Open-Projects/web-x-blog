// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091535
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class solution111 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  static TreeNode constructMaximumBinaryTree(int[] nums) { // 定义函数/方法 constructMaximumBinaryTree
    if (nums.length == 0) return null; // 若 数组.长度 等于 0，直接返回 null
    int idx = 0; // 把 0 存入 idx
    for (int i = 0; i < nums.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (nums[i] > nums[idx]) idx = i; // 若 数组[下标 i] 超过 数组[idx]) idx 赋值为 下标 i;
    }
    TreeNode root = new TreeNode(nums[idx]); // 把 new TreeNode(数组[idx]); 写入 TreeNode root
    root.left = buildLeft(nums, idx); // 把 buildLeft(数组, idx); 写入 左边界
    root.right = buildRight(nums, idx); // 把 buildRight(数组, idx); 写入 右边界
    return root; // 返回 根节点
  }

  static TreeNode buildLeft(int[] nums, int idx) { // 定义函数/方法 buildLeft
    if (idx == 0) return null; // 若 idx 等于 0，直接返回 null
    int[] left = new int[idx]; // 把 new int[idx]; 写入 int[] left
    for (int i = 0; i < idx; i++) left[i] = nums[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 idx 就继续
    return constructMaximumBinaryTree(left); // 返回 constructMaximumBinaryTree(左边界)
  }

  static TreeNode buildRight(int[] nums, int idx) { // 定义函数/方法 buildRight
    if (idx == nums.length - 1) return null; // 若 idx 等于 数组.长度 减 1，直接返回 null
    int len = nums.length - idx - 1; // 把 数组.长度 减 idx 减 1 存入 长度
    int[] right = new int[len]; // 把 new int[长度]; 写入 int[] right
    for (int i = 0; i < len; i++) right[i] = nums[idx + 1 + i]; // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
    return constructMaximumBinaryTree(right); // 返回 constructMaximumBinaryTree(右边界)
  }

  static List<Integer> preorder(TreeNode root, List<Integer> res) { // 定义函数/方法 preorder
    if (root == null) {
      res.add(null);
      return res;
    } // 若 根节点 等于 null) { 结果 追加 null); return 结果; }
    res.add(root.val); // 结果 追加 根节点.值);
    preorder(root.left, res); // preorder(根节点.左边界, 结果);
    preorder(root.right, res); // preorder(根节点.右边界, 结果);
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    solution111 s = new solution111(); // 把 new solution111(); 写入 solution111 s
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {
        new int[] {3, 2, 1, 6, 0, 5},
        Arrays.asList(6, 3, null, 2, null, 1, null, null, 5, 0, null, null, null)
      },
      {new int[] {3, 2, 1}, Arrays.asList(3, null, 2, null, 1, null, null)},
      {new int[] {}, Arrays.asList((Integer) null)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
      List<Integer> want =
          (List<Integer>) c[1]; // 把 (List 小于 Integer 超过 ) 字符[1]; 写入 List<Integer> want
      List<Integer> got = s.preorder(s.constructMaximumBinaryTree((int[]) c[0]), new ArrayList<>());
      if (!got.equals(want)) { // 若 取反 got.equals(want
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL constructMaximumBinaryTree got=" + got + " want=" + want); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
