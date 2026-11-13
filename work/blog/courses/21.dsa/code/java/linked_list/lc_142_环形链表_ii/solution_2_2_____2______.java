// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094299
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc142_solution222 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode() {} // ListNode() {}

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  static ListNode detectCycle(ListNode head) { // 定义函数/方法 detectCycle
    if (head == null) return null; // 若 头节点 等于 null，直接返回 null
    ListNode slow = head, fast = head; // 把 头节点, 快指针 赋值为 头节点; 写入 ListNode slow
    while (fast != null) { // 循环，直到不满足「快指针 不等于 null」
      slow = slow.next; // 把 慢指针.下一个; 写入 慢指针
      if (fast.next == null) return null; // 若 快指针.下一个 等于 null，直接返回 null
      fast = fast.next.next; // 把 快指针.下一个.下一个; 写入 快指针
      if (fast == slow) { // 若 快指针 等于 慢指针
        ListNode ptr = head; // 把 头节点; 写入 ListNode ptr
        while (ptr != slow) {
          ptr = ptr.next;
          slow = slow.next;
        } // 循环，直到不满足「ptr 不等于 慢指针) { ptr 赋值为 ptr.下一个; 慢指针 赋值为 慢指针.下一个; }」
        return ptr; // 返回 ptr
      }
    }
    return null; // 返回 null
  }

  static ListNode build(int[] a) { // 定义函数/方法 build
    ListNode dummy = new ListNode(0),
        cur = dummy; // 把 new ListNode(0), 当前值 赋值为 哨兵节点; 写入 ListNode dummy
    for (int v : a) {
      cur.next = new ListNode(v);
      cur = cur.next;
    } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  static ListNode nodeAt(ListNode h, int idx) {
    for (int i = 0; i < idx; i++) h = h.next;
    return h;
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc142_solution222 s =
        new lc142_solution222(); // 把 new lc142_solution222(); 写入 lc142_solution222 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.detectCycle(build(new int[] {1, 2, 3})) != null) {
      ok = false;
      System.out.println("FAIL no-cycle");
    }
    ListNode h2 =
        build(new int[] {3, 2, 0, -4}); // 把 build(new int[]{3, 2, 0, 减 4}); 写入 ListNode h2
    nodeAt(h2, 3).next = nodeAt(h2, 1); // 把 nodeAt(h2, 1); 写入 下一个
    ListNode r2 = s.detectCycle(h2); // 把 字符串.detectCycle(h2); 写入 ListNode r2
    if (r2 == null || r2.val != 2) {
      ok = false;
      System.out.println("FAIL cycle got " + (r2 == null ? "null" : r2.val));
    }
    if (s.detectCycle(null) != null) {
      ok = false;
      System.out.println("FAIL null");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
