// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094075
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc92_solution333 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode() {} // ListNode() {}

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  public ListNode reverseBetween(ListNode head, int left, int right) { // 定义函数/方法 reverseBetween
    ListNode dummy = new ListNode(0); // 把 new ListNode(0); 写入 ListNode dummy
    dummy.next = head; // 把 头节点; 写入 下一个
    ListNode pre = dummy; // 把 哨兵节点; 写入 ListNode pre
    for (int i = 0; i < left - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 左边界 减 1 就继续
      pre = pre.next; // 把 前缀和.下一个; 写入 前缀和
    }
    ListNode cur = pre.next; // 把 前缀和.下一个; 写入 ListNode cur
    for (int i = 0; i < right - left; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 右边界 减 左边界 就继续
      ListNode next = cur.next; // 把 当前值.下一个; 写入 ListNode next
      cur.next = next.next; // 把 下一个.下一个; 写入 下一个
      next.next = pre.next; // 把 前缀和.下一个; 写入 下一个
      pre.next = next; // 把 下一个; 写入 下一个
    }
    return dummy.next; // 返回 哨兵节点.下一个
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
    while (a != null && b != null) {
      if (a.val != b.val) return false;
      a = a.next;
      b = b.next;
    }
    return a == null && b == null; // 返回 数组 等于 null 且 b 等于 null
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc92_solution333 s = new lc92_solution333(); // 把 new lc92_solution333(); 写入 lc92_solution333 s
    Object[] t1 = new Object[] {new int[] {1, 2, 3, 4, 5}, 2, 4, new int[] {1, 4, 3, 2, 5}};
    Object[] t2 = new Object[] {new int[] {1, 2, 3}, 1, 3, new int[] {3, 2, 1}};
    Object[] t3 = new Object[] {new int[] {1, 2, 3}, 1, 1, new int[] {1, 2, 3}};
    Object[][] tests = {t1, t2, t3}; // 把 {t1, t2, t3}; 写入 Object[][] tests
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] t : tests) { // for (Object[] 另一字符串 : tests) {
      int[] inp = (int[]) t[0]; // 把 (int[]) 另一字符串[0]; 写入 int[] inp
      int l = (int) t[1]; // 把 (int) 另一字符串[1] 存入 左指针
      int r = (int) t[2]; // 把 (int) 另一字符串[2] 存入 右指针
      int[] want = (int[]) t[3]; // 把 (int[]) 另一字符串[3]; 写入 int[] want
      ListNode got =
          s.reverseBetween(
              build(inp), l, r); // 把 字符串.reverseBetween(build(inp), 左指针, 右指针); 写入 ListNode got
      if (!eqList(got, build(want))) { // 若 取反 eqList(got, build(want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL reverseBetween("
                + Arrays.toString(inp)
                + ","
                + l
                + ","
                + r
                + ")="
                + toList(got)
                + " want "
                + Arrays.toString(want)); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
