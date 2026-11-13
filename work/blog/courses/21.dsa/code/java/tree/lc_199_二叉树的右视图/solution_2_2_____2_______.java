// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145030731
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class TreeNode2 { // 定义类型
  int val; // int 值;
  TreeNode2 left; // TreeNode2 左边界;
  TreeNode2 right; // TreeNode2 右边界;

  TreeNode2(int v) {
    val = v;
  } // 把 值; } 写入 TreeNode2(int v) { val

  TreeNode2(int v, TreeNode2 l, TreeNode2 r) {
    val = v;
    left = l;
    right = r;
  }
}

class Main { // 定义类型
  List<Integer> result = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> result

  void dfs(TreeNode2 node, int depth) { // 定义函数/方法 dfs
    if (node == null) return; // 若 节点 等于 null) return;
    if (depth == result.size()) result.add(node.val); // 若 深度 等于 结果.大小()) 结果 追加 节点.值);
    dfs(node.right, depth + 1); // dfs(节点.右边界, 深度 加 1);
    dfs(node.left, depth + 1); // dfs(节点.左边界, 深度 加 1);
  }

  List<Integer> rightSideView(TreeNode2 root) { // 定义函数/方法 rightSideView
    result = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 结果
    dfs(root, 0); // dfs(根节点, 0);
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
    TreeNode2 r1 =
        new TreeNode2(
            1, new TreeNode2(2, null, new TreeNode2(5)), new TreeNode2(3, null, new TreeNode2(4)));
    TreeNode2 r2 = null; // 把 null; 写入 TreeNode2 r2
    TreeNode2 r3 = new TreeNode2(1); // 把 new TreeNode2(1); 写入 TreeNode2 r3
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {r1, Arrays.asList(1, 3, 4)},
      {r2, new ArrayList<Integer>()},
      {r3, Arrays.asList(1)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      List<Integer> got =
          s.rightSideView(
              (TreeNode2) c[0]); // 把 字符串.rightSideView((TreeNode2) 字符[0]); 写入 List<Integer> got
      if (!eqList(got, (List<Integer>) c[1])) { // 若 取反 eqList(got, (List 小于 Integer 超过 ) 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL rightSideView got=" + got + " want=" + c[1]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
