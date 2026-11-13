// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
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

  static ListNode addTwoNumbers(ListNode l1, ListNode l2) { // 定义函数/方法 addTwoNumbers
    ListNode d = new ListNode();
    ListNode p = d;
    int carry = 0;
    while (l1 != null || l2 != null || carry != 0) {
      int s = carry;
      if (l1 != null) {
        s += l1.val;
        l1 = l1.next;
      }
      if (l2 != null) {
        s += l2.val;
        l2 = l2.next;
      }
      carry = s / 10;
      p.next = new ListNode(s % 10);
      p = p.next;
    }
    return d.next; // 返回 d.下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] a = {{2, 4, 3}, {0}, {9, 9, 9, 9}};
    int[][] b = {{5, 6, 4}, {0}, {9, 9, 9}};
    int[][] w = {{7, 0, 8}, {0}, {8, 9, 9, 0, 1}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < a.length; i++) {
      int[] got = toArr(addTwoNumbers(build(a[i]), build(b[i])));
      if (!Arrays.equals(got, w[i])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(got));
      }
    } // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
