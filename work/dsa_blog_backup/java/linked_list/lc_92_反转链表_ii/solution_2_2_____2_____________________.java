// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094075
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

  static ListNode reverseBetween(ListNode head, int left, int right) { // 定义函数/方法 reverseBetween
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode pre = dummy;
    for (int i = 1; i < left; i++) pre = pre.next; // 让 下标 i 从 1 开始计数，下标 i 小于 左边界 就继续
    ListNode start = pre.next, then = start.next; // 把 前缀和.下一个, then 赋值为 起点.下一个; 写入 ListNode start
    for (int i = left; i < right; i++) {
      start.next = then.next;
      then.next = pre.next;
      pre.next = then;
      then = start.next;
    } // 让 下标 i 从 左边界 开始计数，下标 i 小于 右边界 就继续
    return dummy.next; // 返回 哨兵节点.下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {{1, 2, 3, 4, 5}, {5}, {1, 2, 3, 4, 5}};
    int[] ls = {2, 1, 1};
    int[] rs = {4, 1, 5};
    int[][] ws = {{1, 4, 3, 2, 5}, {5}, {5, 4, 3, 2, 1}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) {
      int[] got = toArr(reverseBetween(build(ins[i]), ls[i], rs[i]));
      if (!Arrays.equals(got, ws[i])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(got));
      }
    } // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
