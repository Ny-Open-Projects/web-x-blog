// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753362
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc145_solution_9___9 { // 定义类型
  static class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int v) {
      val = v;
    }
  }

  public static List<Integer> postorderTraversal(TreeNode root) {
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    TreeNode dump = new TreeNode(0); // 把 new TreeNode(0); 写入 TreeNode dump
    dump.left = root; // 把 根节点; 写入 左边界
    TreeNode cur = dump; // 把 dump; 写入 TreeNode cur
    while (cur != null) { // 循环，直到不满足「当前值 不等于 null」
      if (cur.left != null) { // 若 当前值.左边界 不等于 null
        TreeNode pred = cur.left; // 把 当前值.左边界; 写入 TreeNode pred
        while (pred.right != null
            && pred.right != cur) { // 循环，直到不满足「pred.右边界 不等于 null 且 pred.右边界 不等于 当前值」
          pred = pred.right; // 把 pred.右边界; 写入 pred
        }
        if (pred.right == null) { // 若 pred.右边界 等于 null
          pred.right = cur; // 把 当前值; 写入 右边界
          cur = cur.left; // 把 当前值.左边界; 写入 当前值
        } else { // 否则
          List<Integer> rev = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> rev
          TreeNode tmp = cur.left; // 把 当前值.左边界; 写入 TreeNode tmp
          while (tmp != pred) { // 循环，直到不满足「临时变量 不等于 pred」
            rev.add(tmp.val); // rev 追加 临时变量.值);
            tmp = tmp.right; // 把 临时变量.右边界; 写入 临时变量
          }
          rev.add(pred.val); // rev 追加 pred.值);
          Collections.reverse(rev); // 反转
          res.addAll(rev); // 结果.addAll(rev);
          pred.right = null; // 把 null; 写入 右边界
          cur = cur.right; // 把 当前值.右边界; 写入 当前值
        }
      } else { // 否则
        cur = cur.right; // 把 当前值.右边界; 写入 当前值
      }
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
      {new Integer[] {1, null, 2, null, 3}, Arrays.asList(3, 2, 1)},
      {new Integer[] {1, 2, 3}, Arrays.asList(2, 3, 1)},
      {new Integer[] {3, 9, 20, null, null, 15, 7}, Arrays.asList(9, 15, 7, 20, 3)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      List<Integer> got =
          postorderTraversal(root); // 把 postorderTraversal(根节点); 写入 List<Integer> got
      @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
      List<Integer> want =
          (List<Integer>) c[1]; // 把 (List 小于 Integer 超过 ) 字符[1]; 写入 List<Integer> want
      if (!got.equals(want)) { // 若 取反 got.equals(want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL postorderTraversal("
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
