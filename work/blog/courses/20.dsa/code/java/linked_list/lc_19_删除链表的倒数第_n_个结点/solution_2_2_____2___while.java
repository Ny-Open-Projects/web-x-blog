// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145093774
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class solution222while { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode() {} // ListNode() {}

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  public ListNode removeNthFromEnd(ListNode head, int n) { // 定义函数/方法 removeNthFromEnd
    ListNode dummy = new ListNode(0); // 把 new ListNode(0); 写入 ListNode dummy
    dummy.next = head; // 把 头节点; 写入 下一个
    ListNode slow = dummy; // 把 哨兵节点; 写入 ListNode slow
    ListNode fast = dummy; // 把 哨兵节点; 写入 ListNode fast
    while (n-- > 0) { // 循环，直到不满足「元素个数 减一 超过 0」
      fast = fast.next; // 把 快指针.下一个; 写入 快指针
    }
    while (fast.next != null) { // 循环，直到不满足「快指针.下一个 不等于 null」
      fast = fast.next; // 把 快指针.下一个; 写入 快指针
      slow = slow.next; // 把 慢指针.下一个; 写入 慢指针
    }
    slow.next = slow.next.next; // 把 慢指针.下一个.下一个; 写入 下一个
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
    solution222while s = new solution222while(); // 把 new solution222while(); 写入 solution222while s
    Object[] t1 = new Object[] {new int[] {1, 2, 3, 4, 5}, 2, new int[] {1, 2, 3, 5}};
    Object[] t2 =
        new Object[] {
          new int[] {1}, 1, new int[] {}
        }; // 把 new Object[]{new int[]{1}, 1, new int[]{}}; 写入 Object[] t2
    Object[] t3 = new Object[] {new int[] {1, 2}, 2, new int[] {2}};
    Object[][] tests2 = {t1, t2, t3}; // 把 {t1, t2, t3}; 写入 Object[][] tests2
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] t : tests2) { // for (Object[] 另一字符串 : tests2) {
      int[] inp = (int[]) t[0]; // 把 (int[]) 另一字符串[0]; 写入 int[] inp
      int n = (int) t[1]; // 把 (int) 另一字符串[1] 存入 元素个数
      int[] want = (int[]) t[2]; // 把 (int[]) 另一字符串[2]; 写入 int[] want
      ListNode got =
          s.removeNthFromEnd(
              build(inp), n); // 把 字符串.removeNthFromEnd(build(inp), 元素个数); 写入 ListNode got
      if (!eqList(got, build(want))) { // 若 取反 eqList(got, build(want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL removeNthFromEnd("
                + Arrays.toString(inp)
                + ","
                + n
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
