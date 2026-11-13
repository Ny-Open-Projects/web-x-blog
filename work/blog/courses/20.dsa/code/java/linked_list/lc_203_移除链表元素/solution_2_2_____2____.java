// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095646
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc203_solution222 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode() {} // ListNode() {}

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  public ListNode removeElements(ListNode head, int val) { // 定义函数/方法 removeElements
    ListNode dummyHead = new ListNode(0); // 把 new ListNode(0); 写入 ListNode dummyHead
    dummyHead.next = head; // 把 头节点; 写入 下一个
    ListNode temp = dummyHead; // 把 dummyHead; 写入 ListNode temp
    while (temp.next != null) { // 循环，直到不满足「临时变量.下一个 不等于 null」
      if (temp.next.val == val) { // 若 临时变量.下一个.值 等于 值
        temp.next = temp.next.next; // 把 临时变量.下一个.下一个; 写入 下一个
      } else { // 否则
        temp = temp.next; // 把 临时变量.下一个; 写入 临时变量
      }
    }
    return dummyHead.next; // 返回 dummyHead.下一个
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
    lc203_solution222 s =
        new lc203_solution222(); // 把 new lc203_solution222(); 写入 lc203_solution222 s
    Object[] t1 = new Object[] {new int[] {1, 2, 6, 3, 4, 5, 6}, 6, new int[] {1, 2, 3, 4, 5}};
    Object[] t2 = new Object[] {new int[] {6, 6, 6}, 6, new int[] {}};
    Object[] t3 = new Object[] {new int[] {1, 2, 3}, 4, new int[] {1, 2, 3}};
    Object[][] tests = {t1, t2, t3}; // 把 {t1, t2, t3}; 写入 Object[][] tests
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] t : tests) { // for (Object[] 另一字符串 : tests) {
      int[] inp = (int[]) t[0]; // 把 (int[]) 另一字符串[0]; 写入 int[] inp
      int val = (int) t[1]; // 把 (int) 另一字符串[1] 存入 值
      int[] want = (int[]) t[2]; // 把 (int[]) 另一字符串[2]; 写入 int[] want
      ListNode got =
          s.removeElements(build(inp), val); // 把 字符串.removeElements(build(inp), 值); 写入 ListNode got
      if (!eqList(got, build(want))) { // 若 取反 eqList(got, build(want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL removeElements("
                + Arrays.toString(inp)
                + ","
                + val
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
