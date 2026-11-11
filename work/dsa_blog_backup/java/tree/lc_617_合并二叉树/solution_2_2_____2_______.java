// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145090998
package com.webfault.dsa; // 引入依赖

class lc617_solution_2_2_____2_______ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public TreeNode mergeTrees(TreeNode root1, TreeNode root2) { // 定义函数/方法 mergeTrees
    if (root1 == null) return root2; // 若 root1 等于 null，直接返回 root2
    if (root2 == null) return root1; // 若 root2 等于 null，直接返回 root1
    TreeNode merged =
        new TreeNode(
            root1.val + root2.val); // 把 new TreeNode(root1.值 加 root2.值); 写入 TreeNode merged
    merged.left = mergeTrees(root1.left, root2.left); // 把 mergeTrees(root1.左边界, root2.左边界); 写入 左边界
    merged.right =
        mergeTrees(root1.right, root2.right); // 把 mergeTrees(root1.右边界, root2.右边界); 写入 右边界
    return merged; // 返回 merged
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

  static java.util.List<Integer> preorder(
      TreeNode root) { // static java.util.List 小于 Integer 超过 preorder(TreeNode 根节点) {
    java.util.List<Integer> res = new java.util.ArrayList<>();
    preorderHelper(root, res); // preorderHelper(根节点, 结果);
    return res; // 返回 结果
  }

  static void preorderHelper(TreeNode node, java.util.List<Integer> res) { // 定义函数/方法 preorderHelper
    if (node == null) {
      res.add(null);
      return;
    } // 若 节点 等于 null) { 结果 追加 null); return; }
    res.add(node.val); // 结果 追加 节点.值);
    preorderHelper(node.left, res); // preorderHelper(节点.左边界, 结果);
    preorderHelper(node.right, res); // preorderHelper(节点.右边界, 结果);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc617_solution_2_2_____2_______ s = new lc617_solution_2_2_____2_______();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {
        new Integer[] {1, 3, 2, 5},
        new Integer[] {2, 1, 3, null, 4, null, 7},
        java.util.Arrays.asList(3, 4, 5, null, null, 4, null, null, 5, null, 7, null, null)
      },
      {new Integer[] {1}, new Integer[] {2}, java.util.Arrays.asList(3, null, null)},
      {null, new Integer[] {1}, java.util.Arrays.asList(1, null, null)},
      {new Integer[] {1}, null, java.util.Arrays.asList(1, null, null)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode t1 = c[0] == null ? null : build((Integer[]) c[0]);
      TreeNode t2 = c[1] == null ? null : build((Integer[]) c[1]);
      java.util.List<Integer> got = preorder(s.mergeTrees(t1, t2));
      @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
      java.util.List<Integer> want = (java.util.List<Integer>) c[2];
      if (!got.equals(want)) { // 若 取反 got.equals(want
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL mergeTrees got=" + got + " want=" + want); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
