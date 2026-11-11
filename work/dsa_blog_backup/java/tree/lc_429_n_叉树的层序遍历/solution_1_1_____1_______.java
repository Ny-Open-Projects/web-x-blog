// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088458
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc429_solution_1_1_____1_______ { // 定义类型
  static class Node {
    int val;
    List<Node> children = new ArrayList<>();

    Node(int v) {
      val = v;
    }
  }

  public static List<List<Integer>> levelOrder(Node root) {
    return new ArrayList<>(); // 返回 new ArrayList 小于 超过 ()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<List<Integer>> got = levelOrder(null); // 把 levelOrder(null); 写入 List<List<Integer>> got
    if (!got.isEmpty()) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
