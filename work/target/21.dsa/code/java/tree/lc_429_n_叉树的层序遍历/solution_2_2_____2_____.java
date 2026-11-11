// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088458
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc429_solution_2_2_____2_____ { // 定义类型
  static class Node { // static class Node {
    int val; // int 值;
    List<Node> children; // List 小于 Node 超过 children;

    Node(int v) {
      val = v;
      children = new ArrayList<>();
    }
  }

  public List<List<Integer>> levelOrder(Node root) { // 定义函数/方法 levelOrder
    return new ArrayList<>(); // 返回 new ArrayList 小于 超过 ()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc429_solution_2_2_____2_____ s = new lc429_solution_2_2_____2_____();
    List<List<Integer>> got =
        s.levelOrder(null); // 把 字符串.levelOrder(null); 写入 List<List<Integer>> got
    if (!got.isEmpty()) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
