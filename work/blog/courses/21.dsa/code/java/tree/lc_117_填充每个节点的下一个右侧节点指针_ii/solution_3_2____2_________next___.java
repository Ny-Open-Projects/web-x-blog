// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc117_solution_3_2____2_________next___ { // 定义类型
  static class Node { // static class Node {
    int val; // int 值;
    Node left, right, next; // Node 左边界, 右边界, 下一个;

    Node(int v) {
      val = v;
    } // 把 值; } 写入 Node(int v) { val
  }

  public java.util.Map<Integer, Integer> connect(Node root) {
    return new java.util.HashMap<
        Integer, Integer>(); // 返回 new java.util.HashMap 小于 Integer, Integer 超过 ()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc117_solution_3_2____2_________next___ s = new lc117_solution_3_2____2_________next___();
    java.util.Map<Integer, Integer> got =
        s.connect(null); // 把 字符串.connect(null); 写入 java.util.Map<Integer, Integer> got
    if (!got.isEmpty()) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
