// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089820
package com.webfault.dsa; // 引入依赖

class solution_2_2_____2______________ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public boolean isSubtree(TreeNode root, TreeNode subRoot) { // 定义判定函数 isSubtree
    if (root == null) return false; // 若 根节点 等于 null，直接返回 false
    return isSame(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
  }

  private boolean isSame(TreeNode p, TreeNode q) { // 定义判定函数 isSame
    if (p == null && q == null) return true; // 若 节点 等于 null 且 节点 等于 null，直接返回 true
    if (p == null || q == null) return false; // 若 节点 等于 null 或 节点 等于 null，直接返回 false
    if (p.val != q.val) return false; // 若 节点.值 不等于 节点.值，直接返回 false
    return isSame(p.left, q.left)
        && isSame(p.right, q.right); // 返回 isSame(节点.左边界, 节点.左边界) 且 isSame(节点.右边界, 节点.右边界)
  }

  static TreeNode build(Integer[] vals) { // 定义函数/方法 build
    if (vals.length == 0 || vals[0] == null)
      return null; // 若 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    java.util.Queue<TreeNode> q = new java.util.ArrayDeque<>();
    q.offer(root); // 节点.offer(根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!q.isEmpty() && i < vals.length) { // 循环，直到不满足「取反 节点.isEmpty() 且 下标 i 小于 vals.长度」
      TreeNode n = q.poll(); // 把 节点.poll(); 写入 TreeNode n
      if (i < vals.length && vals[i] != null) { // 若 下标 i 小于 vals.长度 且 vals[下标 i] 不等于 null
        n.left = new TreeNode(vals[i]); // 把 new TreeNode(vals[下标 i]); 写入 左边界
        q.offer(n.left); // 节点.offer(元素个数.左边界);
      }
      i++; // 下标 i 加一
      if (i < vals.length && vals[i] != null) { // 若 下标 i 小于 vals.长度 且 vals[下标 i] 不等于 null
        n.right = new TreeNode(vals[i]); // 把 new TreeNode(vals[下标 i]); 写入 右边界
        q.offer(n.right); // 节点.offer(元素个数.右边界);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    solution_2_2_____2______________ s = new solution_2_2_____2______________();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new Integer[] {3, 4, 5, 1, 2}, new Integer[] {4, 1, 2}, Boolean.TRUE},
      {
        new Integer[] {3, 4, 5, 1, 2, null, null, null, null, 0},
        new Integer[] {4, 1, 2},
        Boolean.FALSE
      },
      {null, null, Boolean.FALSE},
      {new Integer[] {1, 1}, new Integer[] {1}, Boolean.TRUE},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      TreeNode sub = c[1] == null ? null : build((Integer[]) c[1]);
      boolean got = s.isSubtree(root, sub); // 把 字符串.isSubtree(根节点, sub); 写入 boolean got
      boolean want = (Boolean) c[2]; // 把 (Boolean) 字符[2]; 写入 boolean want
      if (got != want) { // 若 got 不等于 want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL isSubtree case="
                + java.util.Arrays.toString((Integer[]) c[0])
                + " got="
                + got
                + " want="
                + want); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
