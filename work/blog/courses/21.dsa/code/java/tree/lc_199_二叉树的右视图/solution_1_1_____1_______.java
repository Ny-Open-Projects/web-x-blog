// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145030731
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class TreeNode { // 定义类型
  int val; // int 值;
  TreeNode left; // TreeNode 左边界;
  TreeNode right; // TreeNode 右边界;

  TreeNode(int v) {
    val = v;
  } // 把 值; } 写入 TreeNode(int v) { val

  TreeNode(int v, TreeNode l, TreeNode r) {
    val = v;
    left = l;
    right = r;
  }
}

class Main { // 定义类型
  List<Integer> rightSideView(TreeNode root) { // 定义函数/方法 rightSideView
    if (root == null) return new ArrayList<>(); // 若 根节点 等于 null，直接返回 new ArrayList 小于 超过 ()
    List<Integer> result = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> result
    Deque<TreeNode> queue =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> queue
    queue.add(root); // 队列 追加 根节点);
    while (!queue.isEmpty()) { // 循环，直到不满足「取反 队列.isEmpty(」
      int levelSize = queue.size(); // 把 队列.大小() 存入 levelSize
      for (int i = 0; i < levelSize; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 levelSize 就继续
        TreeNode node = queue.poll(); // 把 队列.poll(); 写入 TreeNode node
        if (i == levelSize - 1) result.add(node.val); // 若 下标 i 等于 levelSize 减 1) 结果 追加 节点.值);
        if (node.left != null) queue.add(node.left); // 若 节点.左边界 不等于 null) 队列 追加 节点.左边界);
        if (node.right != null) queue.add(node.right); // 若 节点.右边界 不等于 null) 队列 追加 节点.右边界);
      }
    }
    return result; // 返回 结果
  }

  static boolean eqList(List<Integer> a, List<Integer> b) { // 定义函数/方法 eqList
    if (a == null || b == null) return a == b; // 若 数组 等于 null 或 b 等于 null，直接返回 数组 等于 b
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    for (int i = 0; i < a.size(); i++)
      if (!a.get(i).equals(b.get(i))) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    // case 1: [1,2,3,null,5,null,4]
    TreeNode r1 =
        new TreeNode(
            1, new TreeNode(2, null, new TreeNode(5)), new TreeNode(3, null, new TreeNode(4)));
    // case 2: empty
    TreeNode r2 = null; // 把 null; 写入 TreeNode r2
    // case 3: single node
    TreeNode r3 = new TreeNode(1); // 把 new TreeNode(1); 写入 TreeNode r3
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {r1, Arrays.asList(1, 3, 4)},
      {r2, new ArrayList<Integer>()},
      {r3, Arrays.asList(1)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      List<Integer> got =
          s.rightSideView(
              (TreeNode) c[0]); // 把 字符串.rightSideView((TreeNode) 字符[0]); 写入 List<Integer> got
      if (!eqList(got, (List<Integer>) c[1])) { // 若 取反 eqList(got, (List 小于 Integer 超过 ) 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL rightSideView got=" + got + " want=" + c[1]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
