// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134622591
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc100_solution_2___2 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public boolean isSameTree(TreeNode p, TreeNode q) { // 定义判定函数 isSameTree
    if (p == null && q == null) return true; // 若 节点 等于 null 且 节点 等于 null，直接返回 true
    if (p == null || q == null) return false; // 若 节点 等于 null 或 节点 等于 null，直接返回 false
    Deque<TreeNode> queue1 =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> queue1
    Deque<TreeNode> queue2 =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> queue2
    queue1.add(p); // queue1 追加 节点);
    queue2.add(q); // queue2 追加 节点);
    while (!queue1.isEmpty()
        && !queue2.isEmpty()) { // 循环，直到不满足「取反 queue1.isEmpty() 且 取反 queue2.isEmpty(」
      TreeNode pTop = queue1.poll(); // 把 queue1.poll(); 写入 TreeNode pTop
      TreeNode qTop = queue2.poll(); // 把 queue2.poll(); 写入 TreeNode qTop
      if (pTop.val != qTop.val) return false; // 若 pTop.值 不等于 qTop.值，直接返回 false
      TreeNode pLeft = pTop.left,
          pRight = pTop.right; // 把 pTop.左边界, pRight 赋值为 pTop.右边界; 写入 TreeNode pLeft
      TreeNode qLeft = qTop.left,
          qRight = qTop.right; // 把 qTop.左边界, qRight 赋值为 qTop.右边界; 写入 TreeNode qLeft
      if ((pLeft != null && qLeft == null) || (pLeft == null && qLeft != null)) return false;
      if ((pRight != null && qRight == null) || (pRight == null && qRight != null)) return false;
      if (pLeft != null) queue1.add(pLeft); // 若 pLeft 不等于 null) queue1 追加 pLeft);
      if (pRight != null) queue1.add(pRight); // 若 pRight 不等于 null) queue1 追加 pRight);
      if (qLeft != null) queue2.add(qLeft); // 若 qLeft 不等于 null) queue2 追加 qLeft);
      if (qRight != null) queue2.add(qRight); // 若 qRight 不等于 null) queue2 追加 qRight);
    }
    return queue1.isEmpty() && queue2.isEmpty(); // 返回 queue1.isEmpty() 且 queue2.isEmpty()
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
    lc100_solution_2___2 s =
        new lc100_solution_2___2(); // 把 new lc100_solution_2___2(); 写入 lc100_solution_2___2 s
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, null, true},
      {new Integer[] {1, 2, 3}, new Integer[] {1, 2, 3}, true},
      {new Integer[] {1, 2}, new Integer[] {1, null, 2}, false},
      {new Integer[] {1, 2, 1}, new Integer[] {1, 1, 2}, false},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode p = c[0] == null ? null : build((Integer[]) c[0]);
      TreeNode q = c[1] == null ? null : build((Integer[]) c[1]);
      boolean got = s.isSameTree(p, q); // 把 字符串.isSameTree(节点, 节点); 写入 boolean got
      if (got != (Boolean) c[2]) { // 若 got 不等于 (Boolean) 字符[2]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL isSameTree("
                + Arrays.toString((Integer[]) c[0])
                + ","
                + Arrays.toString((Integer[]) c[1])
                + ")="
                + got
                + " want "
                + c[2]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
