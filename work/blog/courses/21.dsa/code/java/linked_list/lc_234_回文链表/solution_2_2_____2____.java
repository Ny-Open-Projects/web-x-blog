// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096059
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ListNode {
  int val;
  ListNode next;

  ListNode() {}

  ListNode(int v) {
    val = v;
  }

  ListNode(int v, ListNode n) {
    val = v;
    next = n;
  }
} // 定义类型

class Main { // 定义类型
  static boolean isPalindrome(ListNode head) { // 定义判定函数 isPalindrome
    List<Integer> vals = new ArrayList<>();
    for (ListNode x = head; x != null; x = x.next) vals.add(x.val);
    int i = 0, j = vals.size() - 1;
    while (i < j) {
      if (!vals.get(i).equals(vals.get(j))) return false;
      i++;
      j--;
    }
    return true;
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] ins = {{{1, 2, 2, 1}}, {{1, 2}}, {{}}, {{1}}};
    boolean[] ws = {true, false, true, true};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) {
      ListNode d = new ListNode();
      ListNode p = d;
      for (int v : ins[i][0]) {
        p.next = new ListNode(v);
        p = p.next;
      }
      boolean got = isPalindrome(d.next);
      if (got != ws[i]) {
        ok = false;
        System.out.println("FAIL " + got);
      }
    } // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
