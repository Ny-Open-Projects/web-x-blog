// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091535
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class solution333 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left; // TreeNode 左边界;
    TreeNode right; // TreeNode 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public TreeNode constructMaximumBinaryTree(int[] nums) { // 定义函数/方法 constructMaximumBinaryTree
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n == 0) return null; // 若 元素个数 等于 0，直接返回 null
    TreeNode[] tree = new TreeNode[n]; // 把 new TreeNode[元素个数]; 写入 TreeNode[] tree
    for (int i = 0; i < n; i++) tree[i] = new TreeNode(nums[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    Deque<Integer> stack = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> stack
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      while (!stack.isEmpty()
          && nums[i] > nums[stack.peek()]) { // 循环，直到不满足「取反 栈.isEmpty() 且 数组[下标 i] 超过 数组[栈.peek()]」
        tree[i].left = tree[stack.pop()]; // 弹出栈顶元素
      }
      if (!stack.isEmpty()) { // 若 取反 栈.isEmpty(
        tree[stack.peek()].right = tree[i]; // 把 tree[下标 i]; 写入 右边界
      }
      stack.push(i); // 把 下标 i 压入栈/数组尾部
    }
    return tree[stack.peekLast()]; // 返回 tree[栈.peekLast()]
  }

  private List<Integer> preorder(TreeNode root, List<Integer> res) { // 定义函数/方法 preorder
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
    solution333 s = new solution333(); // 把 new solution333(); 写入 solution333 s
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
