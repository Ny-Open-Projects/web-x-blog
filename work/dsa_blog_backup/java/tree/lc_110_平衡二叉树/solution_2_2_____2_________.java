// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144994166
package com.webfault.dsa; // 引入依赖

class lc110_solution_2_2_____2_________ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left; // TreeNode 左边界;
    TreeNode right; // TreeNode 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public boolean isBalanced(TreeNode root) { // 定义判定函数 isBalanced
    return check(root) != -1; // 返回 check(根节点) 不等于 减 1
  }

  private int check(TreeNode node) { // 定义判定函数 check
    if (node == null) return 0; // 若 节点 等于 null，直接返回 0
    int left = check(node.left); // 把 check(节点.左边界) 存入 左边界
    if (left == -1) return -1; // 若 左边界 等于 减 1，直接返回 减 1
    int right = check(node.right); // 把 check(节点.右边界) 存入 右边界
    if (right == -1) return -1; // 若 右边界 等于 减 1，直接返回 减 1
    if (Math.abs(left - right) > 1) return -1; // 若 Math.取绝对值 左边界 减 右边界) 超过 1，直接返回 减 1
    return Math.max(left, right) + 1; // 返回 Math.取较大值 左边界, 右边界) 加 1
  }

  static TreeNode build(Integer[] a) { // 定义函数/方法 build
    if (a.length == 0 || a[0] == null) return null; // 若 数组.长度 等于 0 或 数组[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(a[0]); // 把 new TreeNode(数组[0]); 写入 TreeNode root
    java.util.Deque<TreeNode> queue = new java.util.ArrayDeque<>();
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
    lc110_solution_2_2_____2_________ s = new lc110_solution_2_2_____2_________();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, true},
      {new Integer[] {3, 9, 20, null, null, 15, 7}, true},
      {new Integer[] {1, 2, 2, 3, 3, null, null, 4, 4}, false},
      {new Integer[] {1}, true},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      boolean got = s.isBalanced(root); // 把 字符串.isBalanced(根节点); 写入 boolean got
      if (got != (Boolean) c[1]) { // 若 got 不等于 (Boolean) 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL isBalanced("
                + java.util.Arrays.toString((Integer[]) c[0])
                + ")="
                + got
                + " want "
                + c[1]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
