// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131631290
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals.length == 0 || vals[0] == null)
      return null; // 若 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
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

  // 方案1：自底向上递归，返回 (是否合法, 子树最小值, 子树最大值)
  static boolean isValidBST(TreeNode root) { // 定义判定函数 isValidBST
    return (Boolean) dfs(root)[0]; // 返回 (Boolean) dfs(根节点)[0]
  }

  static Object[] dfs(TreeNode node) { // 定义函数/方法 dfs
    if (node == null) return new Object[] {true, Integer.MAX_VALUE, Integer.MIN_VALUE};
    Object[] l = dfs(node.left); // 把 dfs(节点.左边界); 写入 Object[] l
    Object[] r = dfs(node.right); // 把 dfs(节点.右边界); 写入 Object[] r
    boolean lOk = (Boolean) l[0],
        rOk = (Boolean) r[0]; // 把 (Boolean) 左指针[0], rOk 赋值为 (Boolean) 右指针[0]; 写入 boolean lOk
    int lMin = (Integer) l[1],
        lMax = (Integer) l[2]; // 把 (Integer) 左指针[1], lMax 赋值为 (Integer) 左指针[2] 存入 lMin
    int rMin = (Integer) r[1],
        rMax = (Integer) r[2]; // 把 (Integer) 右指针[1], rMax 赋值为 (Integer) 右指针[2] 存入 rMin
    boolean ok =
        lOk
            && rOk
            && lMax < node.val
            && node.val < rMin; // 把 lOk 且 rOk 且 lMax 小于 节点.值 且 节点.值 小于 rMin; 写入 boolean ok
    int min = Math.min(lMin, node.val); // 把 Math.取较小值 lMin, 节点.值) 存入 min
    int max = Math.max(rMax, node.val); // 把 Math.取较大值 rMax, 节点.值) 存入 max
    return new Object[] {ok, min, max}; // 返回 new Object[]{ok, min, max}
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Integer[][] ins = { // 把 { 写入 Integer[][] ins
      {2, 1, 3},
      {5, 1, 4, null, null, 3, 6},
      {},
      {1},
      {1, 1},
      {10, 5, 15, null, null, 6, 20},
      {3, 1, 5, 0, 2, 4, 6, null, null, null, 3},
    };
    boolean[] wants = {true, false, true, true, false, false, false};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < ins.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 ins.长度 就继续
      boolean got =
          isValidBST(buildTree(ins[k])); // 把 isValidBST(buildTree(ins[下标 k])); 写入 boolean got
      if (got != wants[k]) { // 若 got 不等于 wants[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL isValidBST("
                + java.util.Arrays.toString(ins[k])
                + ")="
                + got
                + " want "
                + wants[k]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
