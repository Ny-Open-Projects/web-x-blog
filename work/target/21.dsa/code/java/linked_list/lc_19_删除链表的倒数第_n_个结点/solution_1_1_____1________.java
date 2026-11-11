// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145093774
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

  static ListNode removeNthFromEnd(ListNode head, int n) { // 定义函数/方法 removeNthFromEnd
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode f = dummy, s = dummy;
    for (int i = 0; i < n; i++) f = f.next; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    while (f.next != null) {
      f = f.next;
      s = s.next;
    } // 循环，直到不满足「f.下一个 不等于 null){f 赋值为 f.下一个;字符串 赋值为 字符串.下一个;}」
    s.next = s.next.next;
    return dummy.next; // 把 字符串.下一个.下一个; return 哨兵节点.下一个; 写入 下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {{1, 2, 3, 4, 5}, {1}, {1, 2}};
    int[] ns = {2, 1, 2};
    int[][] ws = {{1, 2, 3, 5}, {}, {2}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) {
      int[] got = toArr(removeNthFromEnd(build(ins[i]), ns[i]));
      if (!Arrays.equals(got, ws[i])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(got));
      }
    } // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
