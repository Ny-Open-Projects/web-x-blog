// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513986
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

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
  static ListNode build(int[] vals) {
    ListNode d = new ListNode();
    ListNode p = d;
    for (int v : vals) {
      p.next = new ListNode(v);
      p = p.next;
    }
    return d.next;
  }

  static int[] toArr(ListNode h) {
    int n = 0;
    for (ListNode x = h; x != null; x = x.next) n++;
    int[] r = new int[n];
    int i = 0;
    for (; h != null; h = h.next) r[i++] = h.val;
    return r;
  }

  static ListNode deleteDuplicates(ListNode head) {
    if (head == null) return null;
    ListNode cur = head;
    while (cur.next != null) {
      if (cur.next.val == cur.val) cur.next = cur.next.next;
      else cur = cur.next;
    }
    return head;
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {{1, 1, 2}, {1, 1, 2, 3, 3}, {1, 1, 1}};
    int[][] ws = {{1, 2}, {1, 2, 3}, {1}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) {
      int[] got = toArr(deleteDuplicates(build(ins[i])));
      if (!Arrays.equals(got, ws[i])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(got));
      }
    } // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
