// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
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

  static ListNode sortList(ListNode head) { // 定义函数/方法 sortList
    if (head == null || head.next == null) return head; // 若 头节点 等于 null 或 头节点.下一个 等于 null，直接返回 头节点
    ListNode slow = head, fast = head;
    while (fast.next != null && fast.next.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }
    ListNode mid = slow.next;
    slow.next = null; // 把 慢指针.下一个; 慢指针.下一个 赋值为 null; 写入 ListNode mid
    ListNode l = sortList(head),
        r = sortList(mid); // 把 sortList(头节点), 右指针 赋值为 sortList(中点); 写入 ListNode l
    ListNode d = new ListNode(), p = d; // 把 new ListNode(), 节点 赋值为 d; 写入 ListNode d
    while (l != null && r != null) {
      if (l.val <= r.val) {
        p.next = l;
        l = l.next;
      } else {
        p.next = r;
        r = r.next;
      }
      p = p.next;
    }
    p.next = l != null ? l : r;
    return d.next; // 把 左指针 不等于 null?左指针:右指针; return d.下一个; 写入 下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {{4, 2, 1, 3}, {}, {-1, 5, 3, 4, 0}};
    int[][] ws = {{1, 2, 3, 4}, {}, {-1, 0, 3, 4, 5}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) {
      int[] got = toArr(sortList(build(ins[i])));
      if (!Arrays.equals(got, ws[i])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(got));
      }
    } // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
