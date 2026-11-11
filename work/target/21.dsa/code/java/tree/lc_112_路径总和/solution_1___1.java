// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
package com.webfault.dsa; // 引入依赖

/** LeetCode 112. 路径总和 方案1：DFS 累加根到当前节点的和，到达叶子时与 targetSum 比较（对齐博客算法）。 */
class lc112_solution_1 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left; // TreeNode 左边界;
    TreeNode right; // TreeNode 右边界;

    TreeNode(int v) { // TreeNode(int 值) {
      val = v; // 把 值; 写入 值
    }
  }

  boolean hasPathSum(TreeNode root, int targetSum) { // 定义函数/方法 hasPathSum
    if (root == null) return false; // 若 根节点 等于 null，直接返回 false
    boolean[] res = {false}; // 把 {false}; 写入 boolean[] res
    dfs(root, root.val, targetSum, res); // dfs(根节点, 根节点.值, targetSum, 结果);
    return res[0]; // 返回 结果[0]
  }

  private void dfs(TreeNode n, int v, int targetSum, boolean[] res) { // 定义函数/方法 dfs
    if (n.left == null && n.right == null) { // 若 元素个数.左边界 等于 null 且 元素个数.右边界 等于 null
      if (v == targetSum) res[0] = true; // 若 值 等于 targetSum) 结果[0] 赋值为 true;
      return; // return;
    }
    if (n.left != null) dfs(n.left, v + n.left.val, targetSum, res);
    if (n.right != null) dfs(n.right, v + n.right.val, targetSum, res);
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals == null || vals.length == 0 || vals[0] == null)
      return null; // 若 vals 等于 null 或 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    java.util.LinkedList<TreeNode> q = new java.util.LinkedList<>();
    q.add(root); // 节点 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!q.isEmpty() && i < vals.length) { // 循环，直到不满足「取反 节点.isEmpty() 且 下标 i 小于 vals.长度」
      TreeNode node = q.poll(); // 把 节点.poll(); 写入 TreeNode node
      if (i < vals.length && vals[i] != null) {
        node.left = new TreeNode(vals[i]);
        q.add(node.left);
      }
      i++; // 下标 i 加一
      if (i < vals.length && vals[i] != null) {
        node.right = new TreeNode(vals[i]);
        q.add(node.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  static TreeNode buildClassic() { // 定义函数/方法 buildClassic
    TreeNode root = new TreeNode(5); // 把 new TreeNode(5); 写入 TreeNode root
    root.left = new TreeNode(4); // 把 new TreeNode(4); 写入 左边界
    root.right = new TreeNode(8); // 把 new TreeNode(8); 写入 右边界
    root.left.left = new TreeNode(11); // 把 new TreeNode(11); 写入 左边界
    root.left.left.left = new TreeNode(7); // 把 new TreeNode(7); 写入 左边界
    root.left.left.right = new TreeNode(2); // 把 new TreeNode(2); 写入 右边界
    root.right.left = new TreeNode(13); // 把 new TreeNode(13); 写入 左边界
    root.right.right = new TreeNode(4); // 把 new TreeNode(4); 写入 右边界
    root.right.right.right = new TreeNode(1); // 把 new TreeNode(1); 写入 右边界
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc112_solution_1 s = new lc112_solution_1(); // 把 new lc112_solution_1(); 写入 lc112_solution_1 s
    Integer[][] ins = { // 把 { 写入 Integer[][] ins
      {5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1},
      {},
      {1},
      {1, 2},
    };
    int[] targets = {22, 0, 1, 3}; // 把 {22, 0, 1, 3}; 写入 int[] targets
    boolean[] wants = {true, false, true, true}; // 把 {true, false, true, true}; 写入 boolean[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < ins.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 ins.长度 就继续
      boolean got = s.hasPathSum(buildTree(ins[k]), targets[k]);
      if (got != wants[k]) { // 若 got 不等于 wants[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL hasPathSum("
                + java.util.Arrays.toString(ins[k])
                + ","
                + targets[k]
                + ")="
                + got
                + " want "
                + wants[k]); // 打印输出
      }
    }
    // 经典树：命中与不命中各测一组
    if (!s.hasPathSum(buildClassic(), 27)) {
      ok = false;
      System.out.println("FAIL classic 27");
    }
    if (s.hasPathSum(buildClassic(), 20)) {
      ok = false;
      System.out.println("FAIL classic 20");
    }
    if (!s.hasPathSum(buildClassic(), 18)) {
      ok = false;
      System.out.println("FAIL classic 18");
    }
    if (s.hasPathSum(buildClassic(), 1)) {
      ok = false;
      System.out.println("FAIL classic 1");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
