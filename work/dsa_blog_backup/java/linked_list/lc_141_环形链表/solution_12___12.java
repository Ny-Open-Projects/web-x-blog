// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
package com.webfault.dsa; // 引入依赖

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
  static boolean hasCycle(ListNode head) {
    ListNode s = head, f = head;
    while (f != null && f.next != null) {
      s = s.next;
      f = f.next.next;
      if (s == f) return true;
    }
    return false;
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    ListNode a = new ListNode(1);
    a.next = new ListNode(2);
    a.next.next = new ListNode(3);
    if (hasCycle(a)) {
      System.out.println("FAIL acyclic");
      throw new RuntimeException("FAILED");
    }
    ListNode b = new ListNode(1);
    b.next = new ListNode(2);
    b.next.next = new ListNode(3);
    b.next.next.next = b;
    if (!hasCycle(b)) {
      System.out.println("FAIL cycle");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
