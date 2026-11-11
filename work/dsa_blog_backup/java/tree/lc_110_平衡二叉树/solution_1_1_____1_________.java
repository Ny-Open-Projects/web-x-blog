// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144994166
package com.webfault.dsa; // 引入依赖

class lc110_solution_1_1_____1_________ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  static boolean isBalanced(TreeNode root) { // 定义判定函数 isBalanced
    if (root == null) return true; // 若 根节点 等于 null，直接返回 true
    int lh = height(root.left); // 把 height(根节点.左边界) 存入 lh
    int rh = height(root.right); // 把 height(根节点.右边界) 存入 rh
    return Math.abs(lh - rh) <= 1 && isBalanced(root.left) && isBalanced(root.right);
  }

  static int height(TreeNode n) { // 定义函数/方法 height
    if (n == null) return 0; // 若 元素个数 等于 null，直接返回 0
    return Math.max(height(n.left), height(n.right))
        + 1; // 返回 Math.取较大值 height(元素个数.左边界), height(元素个数.右边界)) 加 1
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
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, true},
      {new Integer[] {3, 9, 20, null, null, 15, 7}, true},
      {new Integer[] {1, 2, 2, 3, 3, null, null, 4, 4}, false},
      {new Integer[] {1}, true},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      boolean got = isBalanced(root); // 把 isBalanced(根节点); 写入 boolean got
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
