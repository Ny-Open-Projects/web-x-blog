// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095015
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc160_solution111 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode() {} // ListNode() {}

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  public ListNode getIntersectionNode(
      ListNode headA, ListNode headB) { // 定义函数/方法 getIntersectionNode
    Set<ListNode> visited = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<ListNode> visited
    ListNode temp = headA; // 把 链表 A; 写入 ListNode temp
    while (temp != null) { // 循环，直到不满足「临时变量 不等于 null」
      visited.add(temp); // 已访问集合 追加 临时变量);
      temp = temp.next; // 把 临时变量.下一个; 写入 临时变量
    }
    temp = headB; // 把 链表 B; 写入 临时变量
    while (temp != null) { // 循环，直到不满足「临时变量 不等于 null」
      if (visited.contains(temp)) return temp; // 若 已访问集合 是否包含 临时变量)，直接返回 临时变量
      temp = temp.next; // 把 临时变量.下一个; 写入 临时变量
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
    lc160_solution111 s =
        new lc160_solution111(); // 把 new lc160_solution111(); 写入 lc160_solution111 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.getIntersectionNode(null, null) != null) {
      ok = false;
      System.out.println("FAIL null");
    }
    if (s.getIntersectionNode(build(new int[] {1, 2, 3}), build(new int[] {4, 5})) != null) {
      ok = false;
      System.out.println("FAIL separate");
    }
    ListNode a3 =
        build(new int[] {1, 2, 3, 4, 5}); // 把 build(new int[]{1, 2, 3, 4, 5}); 写入 ListNode a3
    ListNode b3 = build(new int[] {9, 8, 7}); // 把 build(new int[]{9, 8, 7}); 写入 ListNode b3
    ListNode tail3 = b3;
    while (tail3.next != null) tail3 = tail3.next;
    tail3.next = nodeAt(a3, 2); // 把 nodeAt(a3, 2); 写入 下一个
    ListNode r3 =
        s.getIntersectionNode(a3, b3); // 把 字符串.getIntersectionNode(a3, b3); 写入 ListNode r3
    if (r3 == null || r3.val != 3) {
      ok = false;
      System.out.println("FAIL intersect got " + (r3 == null ? "null" : r3.val));
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
