// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145007192
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc114_solution_4_4____4_______ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public void flatten(TreeNode root) { // 定义函数/方法 flatten
    TreeNode curr = root; // 把 根节点; 写入 TreeNode curr
    while (curr != null) { // 循环，直到不满足「当前值 不等于 null」
      if (curr.left != null) { // 若 当前值.左边界 不等于 null
        TreeNode next = curr.left; // 把 当前值.左边界; 写入 TreeNode next
        TreeNode predecessor = next; // 把 下一个; 写入 TreeNode predecessor
        while (predecessor.right != null) { // 循环，直到不满足「predecessor.右边界 不等于 null」
          predecessor = predecessor.right; // 把 predecessor.右边界; 写入 predecessor
        }
        predecessor.right = curr.right; // 把 当前值.右边界; 写入 右边界
        curr.left = null; // 把 null; 写入 左边界
        curr.right = next; // 把 下一个; 写入 右边界
      }
      curr = curr.right; // 把 当前值.右边界; 写入 当前值
    }
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

  static List<Integer> rightList(TreeNode node) { // 定义函数/方法 rightList
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    while (node != null) { // 循环，直到不满足「节点 不等于 null」
      res.add(node.val); // 结果 追加 节点.值);
      node = node.right; // 把 节点.右边界; 写入 节点
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc114_solution_4_4____4_______ s = new lc114_solution_4_4____4_______();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new Integer[] {1, 2, 5, 3, 4, null, 6}, Arrays.asList(1, 2, 3, 4, 5, 6)},
      {new Integer[] {1, 2}, Arrays.asList(1, 2)},
      {new Integer[] {}, Arrays.asList()},
      {new Integer[] {1}, Arrays.asList(1)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = build((Integer[]) c[0]); // 把 build((Integer[]) 字符[0]); 写入 TreeNode root
      s.flatten(root); // 字符串.flatten(根节点);
      List<Integer> got = rightList(root); // 把 rightList(根节点); 写入 List<Integer> got
      @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
      List<Integer> want =
          (List<Integer>) c[1]; // 把 (List 小于 Integer 超过 ) 字符[1]; 写入 List<Integer> want
      if (!got.equals(want)) { // 若 取反 got.equals(want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL flatten("
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
