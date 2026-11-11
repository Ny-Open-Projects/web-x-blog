// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc206_solution11 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode() {} // ListNode() {}

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val

    ListNode(int v, ListNode n) {
      val = v;
      next = n;
    } // 把 值; 下一个 赋值为 元素个数; } 写入 ListNode(int v, ListNode n) { val
  }

  public ListNode reverseList(ListNode head) { // 定义函数/方法 reverseList
    ListNode prev = null; // 把 null; 写入 ListNode prev
    ListNode curr = head; // 把 头节点; 写入 ListNode curr
    while (curr != null) { // 循环，直到不满足「当前值 不等于 null」
      ListNode next = curr.next; // 把 当前值.下一个; 写入 ListNode next
      curr.next = prev; // 把 前一个; 写入 下一个
      prev = curr; // 把 当前值; 写入 前一个
      curr = next; // 把 下一个; 写入 当前值
    }
    return prev; // 返回 前一个
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

  static List<Integer> toList(ListNode h) { // 定义函数/方法 toList
    List<Integer> r = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> r
    while (h != null) {
      r.add(h.val);
      h = h.next;
    } // 循环，直到不满足「h 不等于 null) { 右指针 追加 h.值); h 赋值为 h.下一个; }」
    return r; // 返回 右指针
  }

  static boolean eqList(ListNode a, ListNode b) { // 定义函数/方法 eqList
    while (a != null && b != null) { // 循环，直到不满足「数组 不等于 null 且 b 不等于 null」
      if (a.val != b.val) return false; // 若 数组.值 不等于 b.值，直接返回 false
      a = a.next;
      b = b.next; // 把 数组.下一个; b 赋值为 b.下一个; 写入 数组
    }
    return a == null && b == null; // 返回 数组 等于 null 且 b 等于 null
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc206_solution11 s = new lc206_solution11(); // 把 new lc206_solution11(); 写入 lc206_solution11 s
    int[][][] tests = {{{1, 2, 3}, {3, 2, 1}}, {{}, {}}, {{1}, {1}}, {{1, 2}, {2, 1}}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] t : tests) { // for (int[][] 另一字符串 : tests) {
      ListNode got =
          s.reverseList(build(t[0])); // 把 字符串.reverseList(build(另一字符串[0])); 写入 ListNode got
      ListNode want = build(t[1]); // 把 build(另一字符串[1]); 写入 ListNode want
      if (!eqList(got, want)) { // 若 取反 eqList(got, want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL reverseList("
                + Arrays.toString(t[0])
                + ")="
                + toList(got)
                + " want "
                + Arrays.toString(t[1])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
