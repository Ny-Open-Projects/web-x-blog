// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088842
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc515_solution_2_2_____2_______ { // 定义类型
  static class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int v) {
      val = v;
    }
  }

  public static List<Integer> largestValues(TreeNode root) {
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    if (root == null) return res; // 若 根节点 等于 null，直接返回 结果
    Deque<TreeNode> queue =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> queue
    queue.add(root); // 队列 追加 根节点);
    while (!queue.isEmpty()) { // 循环，直到不满足「取反 队列.isEmpty(」
      int len = queue.size(); // 把 队列.大小() 存入 长度
      int maxVal = Integer.MIN_VALUE; // 把 Integer.MIN_VALUE 存入 maxVal
      while (len > 0) { // 循环，直到不满足「长度 超过 0」
        len -= 1; // 长度累减 1
        TreeNode t = queue.poll(); // 把 队列.poll(); 写入 TreeNode t
        maxVal = Math.max(maxVal, t.val); // 把 Math.取较大值 maxVal, 另一字符串.值); 写入 maxVal
        if (t.left != null) queue.add(t.left); // 若 另一字符串.左边界 不等于 null) 队列 追加 另一字符串.左边界);
        if (t.right != null) queue.add(t.right); // 若 另一字符串.右边界 不等于 null) 队列 追加 另一字符串.右边界);
      }
      res.add(maxVal); // 结果 追加 maxVal);
    }
    return res; // 返回 结果
  }

  static TreeNode build(Integer[] a) { // 定义函数/方法 build
    if (a.length == 0 || a[0] == null) return null; // 若 数组.长度 等于 0 或 数组[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(a[0]); // 把 new TreeNode(数组[0]); 写入 TreeNode root
    Deque<TreeNode> queue =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> queue
    queue.add(root); // 队列 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!queue.isEmpty() && i < a.length) { // 循环，直到不满足「取反 队列.isEmpty() 且 下标 i 小于 数组.长度」
      TreeNode node = queue.poll(); // 把 队列.poll(); 写入 TreeNode node
      if (i < a.length && a[i] != null) {
        node.left = new TreeNode(a[i]);
        queue.add(node.left);
      }
      i++; // 下标 i 加一
      if (i < a.length && a[i] != null) {
        node.right = new TreeNode(a[i]);
        queue.add(node.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, Arrays.asList()},
      {new Integer[] {1, 3, 2, 5, 3, null, 9}, Arrays.asList(1, 3, 9)},
      {new Integer[] {1, 2, 3}, Arrays.asList(1, 3)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      List<Integer> got = largestValues(root); // 把 largestValues(根节点); 写入 List<Integer> got
      @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
      List<Integer> want =
          (List<Integer>) c[1]; // 把 (List 小于 Integer 超过 ) 字符[1]; 写入 List<Integer> want
      if (!got.equals(want)) { // 若 取反 got.equals(want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL largestValues("
                + Arrays.toString((Integer[]) c[0])
                + ")="
                + got
                + " want "
                + want); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
