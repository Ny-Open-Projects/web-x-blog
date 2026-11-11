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

  // 方案2：栈迭代携带 (low, high) 边界
  static boolean isValidBST(TreeNode root) { // 定义判定函数 isValidBST
    if (root == null) return true; // 若 根节点 等于 null，直接返回 true
    java.util.Deque<Object[]> stack = new java.util.ArrayDeque<>();
    stack.push(new Object[] {root, null, null}); // 把 new Object[]{根节点, null, null} 压入栈/数组尾部
    while (!stack.isEmpty()) { // 循环，直到不满足「取反 栈.isEmpty(」
      Object[] t = stack.pop(); // 弹出栈顶元素
      TreeNode node = (TreeNode) t[0]; // 把 (TreeNode) 另一字符串[0]; 写入 TreeNode node
      Integer low = (Integer) t[1]; // 把 (Integer) 另一字符串[1] 存入 low
      Integer high = (Integer) t[2]; // 把 (Integer) 另一字符串[2] 存入 high
      if (low != null && node.val <= low) return false; // 若 low 不等于 null 且 节点.值 不超过 low，直接返回 false
      if (high != null && node.val >= high)
        return false; // 若 high 不等于 null 且 节点.值 不低于 high，直接返回 false
      if (node.right != null)
        stack.push(
            new Object[] {
              node.right, node.val, high
            }); // 若 节点.右边界 不等于 null) 栈 追加 new Object[]{节点.右边界, 节点.值, high});
      if (node.left != null)
        stack.push(
            new Object[] {
              node.left, low, node.val
            }); // 若 节点.左边界 不等于 null) 栈 追加 new Object[]{节点.左边界, low, 节点.值});
    }
    return true; // 返回 true
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
