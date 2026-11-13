// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc2_solution66 { // 定义类型
  static class ListNode {
    int val;
    ListNode next;

    ListNode() {}

    ListNode(int v) {
      val = v;
    }
  }

  static ListNode build(int[] vals) { // 定义函数/方法 build
    ListNode dummy = new ListNode(0),
        cur = dummy; // 把 new ListNode(0), 当前值 赋值为 哨兵节点; 写入 ListNode dummy
    for (int v : vals) {
      cur.next = new ListNode(v);
      cur = cur.next;
    } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  static List<Integer> toList(ListNode head) { // 定义函数/方法 toList
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    while (head != null) {
      res.add(head.val);
      head = head.next;
    } // 循环，直到不满足「头节点 不等于 null) { 结果 追加 头节点.值); 头节点 赋值为 头节点.下一个; }」
    return res; // 返回 结果
  }

  static boolean eqList(ListNode a, ListNode b) { // 定义函数/方法 eqList
    while (a != null && b != null) {
      if (a.val != b.val) return false;
      a = a.next;
      b = b.next;
    }
    return a == null && b == null; // 返回 数组 等于 null 且 b 等于 null
  }

  public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0),
        curr = dummy; // 把 new ListNode(0), 当前值 赋值为 哨兵节点; 写入 ListNode dummy
    int carry = 0; // 把 0 存入 carry
    while (l1 != null || l2 != null) { // 循环，直到不满足「l1 不等于 null 或 l2 不等于 null」
      int v1 = (l1 != null) ? l1.val : 0; // 把 (l1 不等于 null) ? l1.值 : 0 存入 v1
      int v2 = (l2 != null) ? l2.val : 0; // 把 (l2 不等于 null) ? l2.值 : 0 存入 v2
      int total = v1 + v2 + carry; // 把 v1 加 v2 加 carry 存入 总和
      carry = total / 10; // 把 总和 除以 10; 写入 carry
      curr.next = new ListNode(total % 10); // 把 new ListNode(总和 对…取模 10); 写入 下一个
      curr = curr.next; // 把 当前值.下一个; 写入 当前值
      if (l1 != null) l1 = l1.next; // 若 l1 不等于 null) l1 赋值为 l1.下一个;
      if (l2 != null) l2 = l2.next; // 若 l2 不等于 null) l2 赋值为 l2.下一个;
    }
    if (carry != 0)
      curr.next = new ListNode(carry); // 若 carry 不等于 0) 当前值.下一个 赋值为 new ListNode(carry);
    return dummy.next; // 返回 哨兵节点.下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc2_solution66 s = new lc2_solution66(); // 把 new lc2_solution66(); 写入 lc2_solution66 s
    Object[] t1 = new Object[] {new int[] {2, 4, 3}, new int[] {5, 6, 4}, new int[] {7, 0, 8}};
    Object[] t2 = new Object[] {new int[] {0}, new int[] {0}, new int[] {0}};
    Object[] t3 = new Object[] {new int[] {9, 9}, new int[] {1}, new int[] {0, 0, 1}};
    Object[][] tests = {t1, t2, t3}; // 把 {t1, t2, t3}; 写入 Object[][] tests
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] t : tests) { // for (Object[] 另一字符串 : tests) {
      ListNode got = s.addTwoNumbers(build((int[]) t[0]), build((int[]) t[1]));
      if (!eqList(got, build((int[]) t[2]))) { // 若 取反 eqList(got, build((int[]) 另一字符串[2]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL addTwoNumbers("
                + Arrays.toString((int[]) t[0])
                + ","
                + Arrays.toString((int[]) t[1])
                + ")="
                + toList(got)
                + " want "
                + Arrays.toString((int[]) t[2])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
