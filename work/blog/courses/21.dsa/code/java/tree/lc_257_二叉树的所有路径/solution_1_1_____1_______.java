// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083565
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc257_solution_1_1_____1_______ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public List<String> binaryTreePaths(TreeNode root) { // 定义函数/方法 binaryTreePaths
    List<String> paths = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> paths
    constructPaths(root, "", paths); // constructPaths(根节点, 「」, paths);
    return paths; // 返回 paths
  }

  private void constructPaths(
      TreeNode root, String path, List<String> paths) { // 定义函数/方法 constructPaths
    if (root != null) { // 若 根节点 不等于 null
      path += String.valueOf(root.val); // 当前路径累加 String.valueOf(根节点.值)
      if (root.left == null && root.right == null) { // 若 根节点.左边界 等于 null 且 根节点.右边界 等于 null
        paths.add(path); // paths 追加 当前路径);
      } else { // 否则
        path += "->"; // 当前路径累加 「 减 超过 」
        constructPaths(root.left, path, paths); // constructPaths(根节点.左边界, 当前路径, paths);
        constructPaths(root.right, path, paths); // constructPaths(根节点.右边界, 当前路径, paths);
      }
    }
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
    lc257_solution_1_1_____1_______ s = new lc257_solution_1_1_____1_______();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {null, Arrays.asList()},
      {new Integer[] {1}, Arrays.asList("1")},
      {new Integer[] {1, 2, 3, null, 5}, Arrays.asList("1->2->5", "1->3")},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      List<String> got = s.binaryTreePaths(root); // 把 字符串.binaryTreePaths(根节点); 写入 List<String> got
      @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
      List<String> want = (List<String>) c[1]; // 把 (List 小于 String 超过 ) 字符[1]; 写入 List<String> want
      if (!got.equals(want)) { // 若 取反 got.equals(want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL binaryTreePaths("
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
