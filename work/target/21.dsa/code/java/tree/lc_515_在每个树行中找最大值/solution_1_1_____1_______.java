// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088842
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc515_solution_1_1_____1_______ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left; // TreeNode 左边界;
    TreeNode right; // TreeNode 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public List<Integer> largestValues(TreeNode root) { // 定义函数/方法 largestValues
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    if (root == null) return res; // 若 根节点 等于 null，直接返回 结果
    dfs(res, root, 0); // dfs(结果, 根节点, 0);
    return res; // 返回 结果
  }

  private void dfs(List<Integer> res, TreeNode root, int curHeight) { // 定义函数/方法 dfs
    if (curHeight == res.size()) { // 若 curHeight 等于 结果.大小(
      res.add(root.val); // 结果 追加 根节点.值);
    } else { // 否则
      res.set(
          curHeight,
          Math.max(
              res.get(curHeight),
              root.val)); // 结果.set(curHeight, Math.取较大值 结果 查找 curHeight), 根节点.值));
    }
    if (root.left != null)
      dfs(res, root.left, curHeight + 1); // 若 根节点.左边界 不等于 null) dfs(结果, 根节点.左边界, curHeight 加 1);
    if (root.right != null)
      dfs(res, root.right, curHeight + 1); // 若 根节点.右边界 不等于 null) dfs(结果, 根节点.右边界, curHeight 加 1);
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
    lc515_solution_1_1_____1_______ s = new lc515_solution_1_1_____1_______();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, Arrays.asList()},
      {new Integer[] {1, 3, 2, 5, 3, null, 9}, Arrays.asList(1, 3, 9)},
      {new Integer[] {1, 2, 3}, Arrays.asList(1, 3)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      List<Integer> got = s.largestValues(root); // 把 字符串.largestValues(根节点); 写入 List<Integer> got
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
