// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130508569
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
  static int[] toArr(ListNode h) {
    int n = 0;
    for (ListNode x = h; x != null; x = x.next) n++;
    int[] r = new int[n];
    int i = 0;
    for (; h != null; h = h.next) r[i++] = h.val;
    return r;
  }

  static ListNode build(int[] vals) {
    ListNode d = new ListNode();
    ListNode p = d;
    for (int v : vals) {
      p.next = new ListNode(v);
      p = p.next;
    }
    return d.next;
  }

  static void deleteNode(ListNode node) {
    node.val = node.next.val;
    node.next = node.next.next;
  } // 把 节点.下一个.值; 节点.下一个 赋值为 节点.下一个.下一个; } 写入 值

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] vals = {4, 5, 1, 9};
    ListNode head = build(vals);
    ListNode target = head.next;
    deleteNode(target);
    int[] got = toArr(head);
    int[] want = {4, 1, 9}; // 把 toArr(头节点); int[] want 赋值为 {4,1,9}; 写入 int[] got
    if (!Arrays.equals(got, want)) {
      System.out.println("FAIL " + Arrays.toString(got));
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
